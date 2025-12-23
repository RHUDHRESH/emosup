import os
import importlib
import pytest
import config

def test_groq_configuration():
    """Verify that config.py supports Groq configuration."""
    # Reload config to ensure we're testing the latest version
    importlib.reload(config)
    
    # Check for Groq API Key variable (should default to None or empty if not set)
    assert hasattr(config, 'GROQ_API_KEY')
    
    # Check for Model Name (should default to a Groq-supported model)
    assert hasattr(config, 'MODEL_NAME')
    # Default should ideally be a Groq model like llama3-8b-8192 or similar
    
    # Check that Ollama base URL is removed or deprecated
    # We expect OLLAMA_BASE_URL to still exist for backward compatibility 
    # but not be the primary inference source if GROQ_API_KEY is present.
    assert hasattr(config, 'OLLAMA_BASE_URL')

def test_groq_api_key_loading(monkeypatch):
    """Test that GROQ_API_KEY is loaded from environment."""
    test_key = "gsk_test_key_12345"
    monkeypatch.setenv("GROQ_API_KEY", test_key)
    
    importlib.reload(config)
    assert config.GROQ_API_KEY == test_key
