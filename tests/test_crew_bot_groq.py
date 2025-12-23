import os
import pytest
from unittest.mock import MagicMock, patch
from crew_bot import EmotionalSupportCrew

def test_initialization_with_groq_api_key(monkeypatch):
    """Verify that EmotionalSupportCrew initializes ChatGroq when GROQ_API_KEY is present."""
    monkeypatch.setenv("GROQ_API_KEY", "gsk_test_key_54321")
    
    # We need to mock the ChatGroq class because it might not be installed yet
    # and we want to verify it's CALLED.
    with patch('crew_bot.ChatGroq') as mock_chat_groq:
        crew = EmotionalSupportCrew()
        # Verify that ChatGroq was initialized
        assert mock_chat_groq.called
        # Verify it was initialized with correct arguments
        args, kwargs = mock_chat_groq.call_args
        assert kwargs.get('groq_api_key') == "gsk_test_key_54321"

def test_initialization_without_groq_api_key(monkeypatch):
    """Verify that it falls back to Ollama when GROQ_API_KEY is absent."""
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    
    with patch('crew_bot.Ollama') as mock_ollama:
        crew = EmotionalSupportCrew()
        assert mock_ollama.called
