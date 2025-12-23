# 🧠💜 EmoSupport - Your AI Therapy Companion

<<<<<<< Updated upstream
**Professional-grade AI therapist with 5 evidence-based frameworks, long-term memory, and voice interaction.**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-production--ready-green.svg)]()

---

## 🚀 ONE-COMMAND INSTALL (Windows)

```bash
# Download the repo, then:
Double-click: SETUP_AND_RUN.bat
```

**That's it!** The script will ask for your Groq API key (or press ENTER to skip).

See [SIMPLE_INSTALL.md](SIMPLE_INSTALL.md) for full details.

---

## ✨ What You Get

### 💬 Professional AI Therapy
- **5 Evidence-Based Frameworks**: ACT, CBT, DBT, Schema Therapy, Narrative Therapy
- **Crisis Detection**: Immediate safety resources
- **Emotion Analysis**: Detects sad, anxious, lonely, angry, and more
- **Adaptive Responses**: Changes therapy mode based on needs

### 🧠 Long-Term Memory
- **Remembers You**: "Welcome back! Last time we talked about..."
- **Tracks Progress**: Emotional patterns and breakthroughs
- **Cloud Sync**: Optional Supabase (FREE tier)

### 🎤 Voice Interaction
- **Speech-to-Speech**: Talk naturally
- **Interruption Handling**: Stops when you speak
- **Emotion-Aware Voice**: Adapts to your feelings

### 🔒 100% Privacy
- **Local Storage**: All data on YOUR computer
- **Anonymous IDs**: No personal info
- **Offline Mode**: Works without internet

### 🆓 Completely FREE
- No subscriptions
- No credit card
- No ads
- Open source

---

## 📖 Quick Start

### Windows

1. Download ZIP from GitHub
2. Extract anywhere
3. Double-click: `SETUP_AND_RUN.bat`
4. (Optional) Enter Groq API key or press ENTER
5. Opens in browser automatically!

### Linux/Mac

```bash
git clone https://github.com/RHUDHRESH/emosup.git
cd emosup
pip install -r requirements.txt
npm install
npm run build
python api_server.py
# Open: http://localhost:5000
```

---

## 🎯 How It Works

```
You: "I feel really anxious about work"

AI: "I hear that you're carrying anxiety. Can we explore
     what specifically worries you?"

[After a few messages...]

You: "Everyone always leaves me in the end"

AI: "I'm noticing a pattern - this deep fear of abandonment.
     This sounds like an abandonment schema. Here's what's
     important: this belief made sense as protection, but it
     might not reflect reality now. Can you think of even
     ONE person who has NOT left?"
```

---

## 🧪 Tech Stack

- **Backend**: Python 3.10+, Flask, LangChain
- **Frontend**: Next.js 14, TypeScript, Tailwind
- **AI**: Groq API (FREE), Ollama (optional), Built-in responses
- **Storage**: Local JSON, Supabase (optional)
- **Voice**: Web Speech API

---

## 📁 Key Files

- `SETUP_AND_RUN.bat` - One-click installer
- `api_server.py` - Flask API
- `therapy_agent_system.py` - Multi-agent system
- `advanced_therapy_frameworks.py` - 5 frameworks
- `memory_system.py` - Long-term memory
- `app/therapy/page.tsx` - Voice interface

---

## 🔧 Optional: Get FREE Groq API Key

For the **best** AI responses (still FREE!):

1. Go to: https://console.groq.com/keys
2. Sign up (no credit card!)
3. Create API key
4. Run `SETUP_AND_RUN.bat` and paste when asked

**Groq FREE tier:**
- ✅ 30 requests/minute
- ✅ Llama 3.3 70B model
- ✅ No expiration
- ✅ No credit card required

---

## 📊 Features Comparison

| Feature | Without API Key | With Groq Key |
|---------|----------------|---------------|
| AI Therapist | ✅ Built-in | ✅ Llama 3.3 70B |
| Emotion Detection | ✅ | ✅ |
| 5 Therapy Frameworks | ✅ | ✅ |
| Memory System | ✅ | ✅ |
| Voice Interface | ✅ | ✅ |
| Crisis Detection | ✅ | ✅ |
| Works Offline | ✅ | ❌ |
| Response Quality | Good | Excellent |
| Context Awareness | Basic | Advanced |

---

## 🎓 Therapy Frameworks

- **ACT** (Acceptance & Commitment): For anxiety, rumination
- **CBT** (Cognitive Behavioral): For negative thinking
- **DBT** (Dialectical Behavior): For intense emotions
- **Schema Therapy**: For deep patterns and childhood wounds
- **Narrative Therapy**: For identity issues

---

## ⚠️ Disclaimer

**This is NOT a replacement for professional therapy.**

**In Crisis? Contact:**
- 🆘 **988** - National Suicide Prevention (US)
- 📱 **Text HOME to 741741** - Crisis Text Line
- 🌍 **International**: https://www.iasp.info/resources/Crisis_Centres/

---

## 📚 Documentation

- [SIMPLE_INSTALL.md](SIMPLE_INSTALL.md) - Installation guide
- [ADVANCED_FEATURES_SUMMARY.md](ADVANCED_FEATURES_SUMMARY.md) - Feature docs
- [SUPABASE_SETUP.md](SUPABASE_SETUP.md) - Cloud setup
- [REDTEAM_FINDINGS.md](REDTEAM_FINDINGS.md) - Security testing

---

## 🤝 Contributing

Contributions welcome! Areas we'd love help:
- Additional therapy frameworks
- Emotion detection improvements
- Mobile app
- Translations

---

## 📜 License

MIT License - See LICENSE file

---

## 🌟 Star Us!

If EmoSupport helped you, please ⭐ this repo!

---

**Made with 💜 for mental health**

🎉 **One command. 30 seconds. Free forever.** 🎉

```
SETUP_AND_RUN.bat
```

*Your mental health matters.* 💜
=======
An empathetic AI-powered emotional support chatbot built with **CrewAI**, Groq (cloud inference) with optional Ollama fallback, and Streamlit. This application leverages a multi-agent system to provide 24/7 emotional support, mood tracking, and coping strategies to help reduce loneliness and promote mental well-being.

## Features

### Core Features
- **Multi-Agent Intelligence**: Powered by **CrewAI** with specialized agents:
  - **Empathy Analyst**: Detects emotions and sentiment patterns.
  - **Compassionate Companion**: Crafts personalized, supportive responses.
- **24/7 Emotional Support**: AI-powered empathetic conversations using Groq (default) or Ollama models.
- **Emotion Detection**: Real-time emotion analysis integrated into the agent workflow.
- **User Authentication**: Secure login system with encrypted password storage.
- **Mood Tracking**: Track and visualize your emotional patterns over time.
- **Coping Strategies**: Personalized suggestions generated by the Empathy Analyst.
- **Conversation History**: Save and review past conversations with context-aware agents.
- **Crisis Detection**: Identifies crisis situations and provides emergency resources.

### Technical Features
- Built with **CrewAI** for multi-agent orchestration.
- Groq integration for cloud LLM inference (default), with optional Ollama fallback.
- **CI/CD Pipeline**: Integrated GitHub Actions for automated linting and testing.
- **Comprehensive Test Suite**: Unit tests for agents, API, database, and analyzers.
- SQLite database for data persistence.
- Dual Interfaces: Modern React/Next.js frontend and interactive Streamlit UI.
- Sentiment analysis with TextBlob.
- Secure password hashing with bcrypt.

## Installation

### Prerequisites
- Python 3.8 or higher
- Groq API key (recommended for cloud inference)
- Ollama installed on your system (optional fallback)
- At least 8GB RAM (for local models)

### Step 1: Configure Groq (Recommended)

Set `GROQ_API_KEY` in your `.env` file (see Step 8).

### Step 2: Optional - Install Ollama

Download and install Ollama from https://ollama.com

### Step 3: Optional - Pull Gemma Model

```bash
ollama pull gemma2:2b
```

Note: You can also use other local models like `gemma2:9b` by updating the MODEL_NAME in `.env`

### Step 4: Clone/Download Project

```bash
cd C:\Users\hp\OneDrive\Desktop\emosup
```

### Step 5: Create Virtual Environment (Recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Step 6: Install Dependencies

```bash
pip install -r requirements.txt
```

Note: If you encounter issues with `sqlite3`, it usually comes pre-installed with Python. Remove it from requirements.txt if needed.

### Step 7: Download TextBlob Corpora

```bash
python -m textblob.download_corpora
```

### Step 8: Configure Environment

Copy `.env.example` to `.env` and modify if needed:

```bash
copy .env.example .env
```

Default configuration:
```
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=llama3-8b-8192
OLLAMA_BASE_URL=http://localhost:11434
APP_TITLE=Emotional Support Companion
```

## Running the Application

**👉 For detailed step-by-step instructions, see [START_GUIDE.md](START_GUIDE.md)**

### Quick Start (Streamlit App)

1. If using Ollama, start it: `ollama serve` (Groq users can skip)
2. Activate virtual environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux)
3. Run: `streamlit run app.py`
4. Open browser to: `http://localhost:8501`

### Quick Start (Next.js Frontend)

1. Terminal 1: If using Ollama, start it: `ollama serve` (Groq users can skip)
2. Terminal 2: `venv\Scripts\activate` then `python api_server.py`
3. Terminal 3: `npm run dev`
4. Open browser to: `http://localhost:3000`

For complete instructions, troubleshooting, and details about both interfaces, see [START_GUIDE.md](START_GUIDE.md).

## Usage Guide

### First Time Setup

1. **Sign Up**: Create a new account with username, email, and password
2. **Login**: Use your credentials to log in
3. **Start Chatting**: Begin your first conversation

### Using the Chat

1. Type your thoughts and feelings in the chat input
2. The AI will respond with empathy and understanding
3. Emotions are automatically detected and displayed
4. Relevant coping strategies are suggested when needed

### Mood Tracking

1. Navigate to "📊 Mood Tracker" from the sidebar
2. View your emotional patterns over time
3. Analyze emotion distribution and trends
4. Track your progress with statistics

### Coping Resources

1. Access "🌟 Coping Resources" for self-care tips
2. Browse strategies organized by emotion
3. Try breathing exercises for immediate relief
4. Find crisis hotlines if needed

### Profile Management

1. View your profile information in "⚙️ Profile"
2. Access conversation history
3. Load previous conversations to continue

## Project Structure

```
emosup/
├── app.py                  # Main Streamlit application
├── chatbot.py              # Core chatbot logic with LangChain
├── emotion_analyzer.py     # Emotion detection and sentiment analysis
├── database.py             # SQLite database management
├── config.py               # Configuration and settings
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── README.md               # This file
└── data/                   # Database and user data (auto-created)
    ├── emosup.db           # SQLite database
    └── sessions/           # Session files
```

## Database Schema

### Users Table
- user_id (PRIMARY KEY)
- username (UNIQUE)
- email (UNIQUE)
- password_hash
- full_name
- created_at
- last_login

### Conversations Table
- conversation_id (PRIMARY KEY)
- user_id (FOREIGN KEY)
- started_at
- ended_at

### Messages Table
- message_id (PRIMARY KEY)
- conversation_id (FOREIGN KEY)
- role (user/assistant)
- content
- emotion
- sentiment_polarity
- sentiment_subjectivity
- timestamp

### Mood Logs Table
- log_id (PRIMARY KEY)
- user_id (FOREIGN KEY)
- mood_score
- primary_emotion
- notes
- logged_at

## Customization

### Using Different Models

Edit `.env` file:
```
MODEL_NAME=gemma2:9b  # or llama3.2, mistral, etc.
```

### Adjusting Emotion Keywords

Edit `config.py` and modify the `EMOTION_KEYWORDS` dictionary:

```python
EMOTION_KEYWORDS = {
    "sad": ["sad", "down", "depressed", ...],
    "anxious": ["anxious", "worried", ...],
    # Add more emotions
}
```

### Adding Coping Strategies

Edit `config.py` and add to `COPING_STRATEGIES`:

```python
COPING_STRATEGIES = {
    "sad": [
        "Try taking a walk",
        # Add more strategies
    ]
}
```

## Technical Details

### CrewAI Integration

The chatbot uses a multi-agent system:
- **Agents**: Empathy Analyst and Compassionate Companion.
- **Tasks**: Sequential analysis and response generation.
- **Memory**: Context-aware agents that maintain conversation history.

### CI/CD & Testing

- **GitHub Actions**: Automated workflow in `.github/workflows/ci.yml`.
- **Testing Framework**: `pytest` for unit and integration tests.
- **Linting**: `flake8` for code quality enforcement.

### Emotion Detection

Uses a hybrid approach:
1. Keyword-based emotion detection
2. TextBlob sentiment analysis (polarity and subjectivity)
3. Fallback to sentiment-based emotion classification

### Security

- Passwords are hashed using bcrypt
- SQL injection prevention with parameterized queries
- Session-based authentication
- No sensitive data in plain text

## Troubleshooting

### Ollama Connection Error (Local Fallback)

**Problem**: "Failed to connect to Ollama"

**Solution**:
1. Ensure Ollama is running: `ollama serve`
2. Check if model is installed: `ollama list`
3. Verify OLLAMA_BASE_URL in `.env`

### Model Not Found (Ollama)

**Problem**: Model 'gemma2:2b' not found

**Solution**:
```bash
ollama pull gemma2:2b
```

### Slow Responses (Ollama)

**Problem**: Chatbot takes too long to respond

**Solution**:
1. Use a smaller model (gemma2:2b instead of gemma2:9b)
2. Ensure sufficient RAM available
3. Close other applications

### TextBlob Import Error

**Problem**: "No module named 'textblob'"

**Solution**:
```bash
pip install textblob
python -m textblob.download_corpora
```

### Database Locked

**Problem**: "Database is locked"

**Solution**:
1. Close all instances of the app
2. Delete `data/emosup.db.lock` if it exists
3. Restart the application

## Project Background

This project addresses the growing issue of loneliness and lack of accessible emotional support systems. It aligns with multiple UN Sustainable Development Goals:

- **SDG 3**: Good Health and Well-Being
- **SDG 4**: Quality Education (mental health awareness)
- **SDG 10**: Reduced Inequalities (accessible support)
- **SDG 16**: Peace, Justice, and Strong Institutions

## Methodology

1. **Data Collection**: User inputs and emotional responses
2. **Data Preprocessing**: Text cleaning and normalization
3. **Model Development**: LangChain + Groq/Ollama integration
4. **Emotion Analysis**: Hybrid keyword + sentiment approach
5. **Chatbot Framework**: Streamlit-based interactive UI
6. **Integration**: Database, authentication, and analytics

## Expected Results

- Successful emotion identification using NLP
- Empathetic and context-aware responses
- Measurable improvement in user emotional well-being
- High user engagement and satisfaction
- Safe, non-judgmental platform for expression

## Limitations

- Not a replacement for professional mental health care
- AI may occasionally produce imperfect responses
- Requires internet connection for model inference
- Limited to English language support
- Emotion detection based on keywords may not always be accurate

## Future Enhancements

- Multi-language support
- Voice input/output capabilities
- Integration with mental health professionals
- Mobile application
- Group support features
- Advanced emotion recognition using ML models
- Personalized therapy techniques
- Integration with wearables for mood tracking

## References

1. "Therapeutic Potential of Social Chatbots in Alleviating Loneliness and Social Anxiety" (JMIR, 2025)
2. "AI Companions Reduce Loneliness" (Journal of Consumer Research, 2025)
3. "AI Chatbots for Psychological Health for Health Professionals" (JMIR Human Factors, 2025)

## Contributing

This is a mini-project for educational purposes. Contributions and suggestions are welcome!

## Disclaimer

This chatbot is designed for emotional support and companionship. It is NOT a substitute for professional mental health services. If you are experiencing a mental health crisis, please contact:

- National Suicide Prevention Lifeline: 988 (US)
- Crisis Text Line: Text HOME to 741741
- Emergency Services: 911 or your local emergency number

## License

This project is created for academic purposes as part of a CSE mini-project.

## Contact

For questions or feedback about this project, please refer to your project documentation or contact your project advisor.

---

**Built with ❤️ using LangChain, Groq, and Streamlit (Ollama optional)**
>>>>>>> Stashed changes
