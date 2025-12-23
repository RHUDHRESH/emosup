"""
Flask API server for the React/Next frontend

Changes:
- Replaced Ollama connectivity probes with Groq status checks
- Improved health/flight checks for cloud-based inference
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import urllib.request
import urllib.error
import socket
import config
import logging
from time import time

# Improvement 6: Structured Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("API_Server")

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Improvement 7: Basic Rate Limiting State
ip_requests = {}

def check_rate_limit():
    ip = request.remote_addr
    now = time()
    if ip not in ip_requests:
        ip_requests[ip] = []
    # Keep only requests from the last minute
    ip_requests[ip] = [t for t in ip_requests[ip] if now - t < 60]
    if len(ip_requests[ip]) > 30: # 30 requests per minute
        return False
    ip_requests[ip].append(now)
    return True

# Initialize chatbot and emotion analyzer (singleton instances)
chatbot = None
emotion_analyzer = None
db = None

def get_db():
    """Get or create database instance"""
    global db
    if db is None:
        try:
            from database import Database
            db = Database()
        except Exception as e:
            print(f"Error initializing database: {e}")
            return None
    return db

def get_chatbot():
    """Get or create chatbot instance without crashing on import errors"""
    global chatbot
    if chatbot is None:
        try:
            # Lazy import to avoid failing API boot when deps are missing
            from crew_bot import EmotionalSupportCrew  # type: ignore
        except Exception as e:
            print(f"Error importing crew_bot module: {e}")
            return None
        try:
            chatbot = EmotionalSupportCrew()
        except Exception as e:
            print(f"Error initializing chatbot: {e}")
            return None
    return chatbot

def get_emotion_analyzer():
    """Get or create emotion analyzer instance without crashing on import errors"""
    global emotion_analyzer
    if emotion_analyzer is None:
        try:
            from emotion_analyzer import EmotionAnalyzer  # type: ignore
        except Exception as e:
            print(f"Error importing emotion analyzer: {e}")
            return None
        try:
            emotion_analyzer = EmotionAnalyzer()
        except Exception as e:
            print(f"Error initializing emotion analyzer: {e}")
            return None
    return emotion_analyzer

def check_groq_status():
    """Verify Groq API configuration status.
    
    Returns a dict with status and message.
    """
    if config.GROQ_API_KEY:
        return {
            "status": "configured",
            "message": "Groq API key is present",
            "model": config.MODEL_NAME
        }
    return {
        "status": "missing_config",
        "message": "Groq API key is missing. Please set GROQ_API_KEY in .env"
    }

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint; always returns 200 with granular components."""
    status = {
        "status": "healthy",
        "api_server": "running",
        "chatbot": "unknown",
        "groq": "unknown",
        "message": "API server is running",
    }

    # Check Groq configuration
    groq_stat = check_groq_status()
    status["groq"] = groq_stat.get("status", "unknown")

    # Check chatbot status
    try:
        bot = get_chatbot()
        status["chatbot"] = "ready" if bot else "not_initialized"
        
        # Check if actually using an engine
        if bot:
            if bot.llm or bot.groq_client:
                status["llm_engine"] = "active"
            else:
                status["llm_engine"] = "inactive"
                status["status"] = "degraded"
                status["message"] = "Chatbot initialized but no LLM engine active."
        
        if not bot and status["groq"] != "configured":
            status["status"] = "degraded"
            status["message"] = "API OK; Groq not configured. Please add GROQ_API_KEY."
    except Exception as e:
        status["chatbot"] = "error"
        status["status"] = "degraded"
        status["message"] = f"Chatbot error: {str(e)}"

    return jsonify(status), 200

@app.route('/api/flight-check', methods=['GET'])
def flight_check():
    """Comprehensive flight check for all services; always 200 with status fields."""
    checks = {
        "timestamp": __import__('datetime').datetime.now().isoformat(),
        "services": {}
    }

    # API server
    checks["services"]["api_server"] = {
        "status": "online",
        "message": "Flask API server is running"
    }

    # Groq status
    checks["services"]["groq"] = check_groq_status()

    # Chatbot status (lazy init)
    try:
        bot = get_chatbot()
        if bot:
            engine = "Groq" if (bot.llm or bot.groq_client) else "None"
            checks["services"]["chatbot"] = {
                "status": "ready",
                "message": f"Chatbot is initialized using {engine} engine"
            }
        else:
            checks["services"]["chatbot"] = {
                "status": "not_ready",
                "message": "Chatbot not initialized. Check Groq configuration."
            }
    except Exception as e:
        checks["services"]["chatbot"] = {
            "status": "error",
            "message": f"Error initializing chatbot: {str(e)}"
        }

    # Overall
    all_ready = (
        checks["services"].get("api_server", {}).get("status") == "online"
        and checks["services"].get("groq", {}).get("status") == "configured"
        and checks["services"].get("chatbot", {}).get("status") == "ready"
    )
    checks["overall_status"] = "ready" if all_ready else "degraded"
    checks["message"] = "All systems operational" if all_ready else "Some services are not ready"

    return jsonify(checks), 200

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages from frontend"""
    # Improvement 8: Apply Rate Limiting
    if not check_rate_limit():
        logger.warning(f"Rate limit exceeded for IP: {request.remote_addr}")
        return jsonify({"error": "Too many requests. Please take a deep breath and try again later."}), 429

    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        logger.info(f"Received message from {request.remote_addr}")
        
        if not message:
            return jsonify({"error": "Message is required"}), 400
        
        # Get chatbot instance
        bot = get_chatbot()
        if bot is None:
            return jsonify({
                "response": "I apologize, but I'm having trouble connecting to the AI service right now. Please verify the Groq API configuration.",
                "error": "Chatbot initialization failed"
            }), 500
        
        # Get chatbot response (CrewAI returns the structured dict)
        response_data = bot.get_response(message)
        
        # Persistence Logic
        database = get_db()
        if database:
            try:
                # We use a default user_id of 1 if no session is provided 
                user_id = 1 
                conv_id = 1 # Simple default for testing/prototype
                
                # Save user message
                database.save_message(
                    conv_id, "user", message, 
                    response_data.get("emotion"), 
                    0, 0 # placeholders for polarity/subjectivity
                )
                # Save assistant message
                database.save_message(conv_id, "assistant", response_data.get("response"))
                # Log mood
                database.log_mood(user_id, 0, response_data.get("emotion"))
            except Exception as e:
                print(f"Database save error: {e}")
        
        return jsonify({
            "response": response_data.get("response", "I'm here for you. Can you tell me more?"),
            "emotion": response_data.get("emotion"),
            "is_crisis": response_data.get("is_crisis", False),
            "coping_suggestion": response_data.get("coping_suggestion")
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({
            "response": "I'm sorry, I encountered an error. Please try again.",
            "error": str(e)
        }), 500

@app.route('/api/reset', methods=['POST'])
def reset_conversation():
    """Reset the conversation"""
    try:
        bot = get_chatbot()
        if bot:
            bot.reset_conversation()
        return jsonify({"status": "success", "message": "Conversation reset"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask API server on http://localhost:5000")
    print("Cloud Inference enabled via Groq API.")
    app.run(debug=True, port=5000, host='0.0.0.0')