"""
Test script to verify the setup and functionality
"""
import sys
import os


def test_imports():
    """Test if all required packages are installed"""
    print("Testing imports...")
    required_packages = [
        ("langchain", "LangChain"),
        ("streamlit", "Streamlit"),
        ("ollama", "Ollama"),
        ("groq", "Groq"),
        ("textblob", "TextBlob"),
        ("pandas", "Pandas"),
        ("plotly", "Plotly"),
        ("bcrypt", "bcrypt"),
        ("dotenv", "python-dotenv"),
    ]

    all_ok = True
    for package, name in required_packages:
        try:
            __import__(package)
            print(f"  [OK] {name} installed")
        except ImportError:
            print(f"  [FAIL] {name} NOT installed")
            all_ok = False

    return all_ok


def test_ollama_connection():
    """Test Ollama connection"""
    print("\nTesting Ollama connection...")
    try:
        from ollama import Client

        client = Client(host="http://localhost:11434")
        models = client.list()
        print("  [OK] Ollama is running")

        model_names = [model.get("name", "") for model in models.get("models", [])]
        if any("gemma" in name.lower() for name in model_names):
            print("  [OK] Gemma model is installed")
            return True
        print("  [FAIL] Gemma model NOT found")
        print("    Run: ollama pull gemma2:2b")
        return False
    except Exception as e:
        print(f"  [FAIL] Ollama connection failed: {str(e)}")
        print("    Make sure Ollama is running: ollama serve")
        return False


def test_database():
    """Test database functionality"""
    print("\nTesting database...")
    try:
        from database import Database

        test_db = Database("data/test_emosup.db")
        user_id = test_db.create_user(
            "test_user_" + str(os.getpid()),
            f"test_{os.getpid()}@example.com",
            "testpass123",
            "Test User",
        )

        if user_id:
            print("  [OK] Database operations working")
            test_db.close()
            if os.path.exists("data/test_emosup.db"):
                os.remove("data/test_emosup.db")
            return True
        print("  [FAIL] Database user creation failed")
        return False

    except Exception as e:
        print(f"  [FAIL] Database test failed: {str(e)}")
        return False


def test_emotion_analyzer():
    """Test emotion analyzer"""
    print("\nTesting emotion analyzer...")
    try:
        from emotion_analyzer import EmotionAnalyzer

        analyzer = EmotionAnalyzer()
        result = analyzer.analyze_text("I am feeling very happy today!")

        if result and "primary_emotion" in result:
            print("  [OK] Emotion detection working")
            print(f"    Detected emotion: {result['primary_emotion']}")
            print(f"    Sentiment: {result['mood_label']}")
            return True
        print("  [FAIL] Emotion detection failed")
        return False

    except Exception as e:
        print(f"  [FAIL] Emotion analyzer test failed: {str(e)}")
        return False


def test_textblob_data():
    """Test if TextBlob corpora is downloaded"""
    print("\nTesting TextBlob data...")
    try:
        from textblob import TextBlob

        blob = TextBlob("This is a test sentence.")
        _ = blob.sentiment
        print("  [OK] TextBlob corpora available")
        return True
    except Exception as e:
        print(f"  [FAIL] TextBlob corpora missing: {str(e)}")
        print("    Run: python -m textblob.download_corpora")
        return False


def test_config():
    """Test configuration file"""
    print("\nTesting configuration...")
    try:
        import config

        if hasattr(config, "OLLAMA_BASE_URL"):
            print("  [OK] Configuration loaded")
            print(f"    Ollama URL: {config.OLLAMA_BASE_URL}")
            print(f"    Model: {config.MODEL_NAME}")
            return True
        print("  [FAIL] Configuration incomplete")
        return False

    except Exception as e:
        print(f"  [FAIL] Configuration test failed: {str(e)}")
        return False


def test_groq_configuration():
    """Test Groq configuration and dependency"""
    print("\nTesting Groq configuration...")
    try:
        import config

        api_key = (os.getenv("GROQ_API_KEY") or config.GROQ_API_KEY or "").strip()
        if not api_key:
            print("  [FAIL] GROQ_API_KEY is not set")
            print("    Set GROQ_API_KEY in .env")
            return False
        try:
            import groq  # noqa: F401
        except ImportError:
            print("  [FAIL] Groq package not installed")
            print("    Run: pip install groq")
            return False
        print("  [OK] GROQ_API_KEY is set")
        return True
    except Exception as e:
        print(f"  [FAIL] Groq config test failed: {str(e)}")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("Emotional Support Companion - Setup Test")
    print("=" * 60)
    print()

    groq_ok = test_groq_configuration()
    if groq_ok:
        print("\nSkipping Ollama check because Groq is configured.")
        ollama_ok = False
    else:
        ollama_ok = test_ollama_connection()

    backend_ok = groq_ok or ollama_ok

    results = {
        "Imports": test_imports(),
        "TextBlob Data": test_textblob_data(),
        "Configuration": test_config(),
        "Emotion Analyzer": test_emotion_analyzer(),
        "Database": test_database(),
        "Inference Backend": backend_ok,
    }

    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)

    for test_name, result in results.items():
        status = "[OK]" if result else "[FAIL]"
        print(f"{test_name:20s}: {status}")

    print()

    all_passed = all(results.values())

    if all_passed:
        print("All tests passed! Your setup is complete.")
        print("\nYou can now run the application:")
        print("  streamlit run app.py")
    else:
        print("Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("  - Install missing packages: pip install -r requirements.txt")
        print("  - Download TextBlob data: python -m textblob.download_corpora")
        print("  - Add Groq key: set GROQ_API_KEY in .env")
        print("  - Start Ollama: ollama serve")
        print("  - Install Gemma model: ollama pull gemma2:2b")

    print()
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
