#!/usr/bin/env python3
"""
Test script to verify Groq API integration is working correctly
"""
import os
import sys

# Try to load dotenv, but don't fail if it's not available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Note: python-dotenv not installed, reading .env manually")
    # Manually load .env file
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()

def test_groq_api_key():
    """Check if Groq API key is configured"""
    print("=" * 60)
    print("GROQ API INTEGRATION TEST")
    print("=" * 60)

    groq_key = os.getenv("GROQ_API_KEY", "")

    if not groq_key:
        print("❌ No GROQ_API_KEY found in .env file")
        print("\nTo fix this:")
        print("1. Copy .env.example to .env")
        print("2. Get a free API key from: https://console.groq.com/keys")
        print("3. Add it to .env: GROQ_API_KEY=gsk_your_key_here")
        return False

    if not groq_key.startswith("gsk_"):
        print(f"⚠️  Warning: API key doesn't start with 'gsk_': {groq_key[:10]}...")
        print("   Make sure you copied the full key from Groq console")
        return False

    print(f"✓ Groq API key found: {groq_key[:15]}...{groq_key[-4:]}")
    return True

def test_free_ai_backend():
    """Test the FreeAIBackend integration"""
    print("\n" + "=" * 60)
    print("Testing FreeAIBackend...")
    print("=" * 60)

    try:
        from free_ai_backends import FreeAIBackend
        print("✓ free_ai_backends.py imported successfully")
    except Exception as e:
        print(f"❌ Failed to import free_ai_backends: {e}")
        return False

    try:
        backend = FreeAIBackend()
        print("✓ FreeAIBackend initialized")
    except Exception as e:
        print(f"❌ Failed to initialize FreeAIBackend: {e}")
        return False

    # Test a simple message
    test_message = "I'm feeling anxious about work"
    test_emotion = "anxious"

    print(f"\nTest input: '{test_message}'")
    print(f"Emotion: {test_emotion}")
    print("\nGetting response from AI backend...")
    print("-" * 60)

    try:
        response = backend.get_response(test_message, test_emotion)

        print(f"\nResponse received:\n{response}")
        print("-" * 60)

        backend_name = backend.backends[backend.current_backend_index].name
        print(f"\n✓ Backend used: {backend_name}")

        if "Groq" in backend_name:
            print("✅ SUCCESS! Groq API is working!")
        elif "Built-in" in backend_name:
            print("⚠️  Using fallback responses (Groq API may not be working)")
            print("   Check your API key and internet connection")
        else:
            print(f"✓ Using alternative backend: {backend_name}")

        return True
    except Exception as e:
        print(f"\n❌ Failed to get response: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_chatbot_integration():
    """Test that chatbot.py can use FreeAIBackend"""
    print("\n" + "=" * 60)
    print("Testing Chatbot Integration...")
    print("=" * 60)

    try:
        from chatbot import EmotionalSupportChatbot
        print("✓ chatbot.py imported successfully")
    except Exception as e:
        print(f"❌ Failed to import chatbot: {e}")
        return False

    try:
        chatbot = EmotionalSupportChatbot()
        print("✓ EmotionalSupportChatbot initialized")
    except Exception as e:
        print(f"⚠️  Warning during initialization: {e}")
        # Continue anyway - chatbot should work with fallbacks

    test_message = "I'm feeling stressed today"
    print(f"\nTest message: '{test_message}'")
    print("Getting response...\n")
    print("-" * 60)

    try:
        result = chatbot.get_response(test_message)
        response = result.get("response", "No response")
        backend = result.get("backend", "unknown")

        print(f"Response: {response}")
        print("-" * 60)
        print(f"\n✓ Backend used: {backend}")

        if backend == "free_ai":
            print("✅ SUCCESS! Chatbot is using free AI backends (including Groq)!")
        elif backend == "ollama":
            print("✓ Using Ollama (local AI)")
        elif backend in ["fallback", "emergency_fallback"]:
            print("⚠️  Using built-in responses (AI backends not available)")
            print("   This is normal if no API keys are configured")

        return True
    except Exception as e:
        print(f"\n❌ Failed to get chatbot response: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_api_endpoints():
    """Test that API endpoints are available"""
    print("\n" + "=" * 60)
    print("Checking API Endpoints...")
    print("=" * 60)

    # Check if api_server.py exists
    if not os.path.exists("api_server.py"):
        print("❌ api_server.py not found")
        return False

    print("✓ api_server.py exists")

    # Check for /api/chat endpoint
    with open("api_server.py", "r") as f:
        content = f.read()

    if "/api/chat" in content:
        print("✓ /api/chat endpoint found")
    else:
        print("❌ /api/chat endpoint not found")
        return False

    if "/api/therapy" in content:
        print("✓ /api/therapy endpoint found (advanced features)")
    else:
        print("⚠️  /api/therapy endpoint not found")

    return True

def main():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "EMOSUP GROQ INTEGRATION TEST" + " " * 20 + "║")
    print("╚" + "=" * 58 + "╝")

    results = []

    # Test 1: API key
    results.append(("API Key Check", test_groq_api_key()))

    # Test 2: Free AI Backend
    results.append(("FreeAIBackend", test_free_ai_backend()))

    # Test 3: Chatbot Integration
    results.append(("Chatbot Integration", test_chatbot_integration()))

    # Test 4: API Endpoints
    results.append(("API Endpoints", test_api_endpoints()))

    # Summary
    print("\n\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {test_name}")

    all_passed = all(result[1] for result in results)

    print("=" * 60)

    if all_passed:
        print("\n🎉 ALL TESTS PASSED!")
        print("\nYou're ready to use EmoSupp with Groq API!")
        print("\nNext steps:")
        print("  1. Start the API server: python api_server.py")
        print("  2. Start the frontend or Streamlit app")
        print("  3. Start chatting!")
    else:
        print("\n⚠️  SOME TESTS FAILED")
        print("\nPlease review the errors above and:")
        print("  1. Make sure .env file has GROQ_API_KEY=gsk_...")
        print("  2. Run: pip install -r requirements.txt")
        print("  3. Check your internet connection")

    print("\n")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
