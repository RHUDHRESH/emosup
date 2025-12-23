import pytest
from unittest.mock import MagicMock, patch
import json
from crew_bot import EmotionalSupportCrew

@pytest.fixture
def mock_crew():
    with patch('crew_bot.Ollama') as mock_ollama:
        bot = EmotionalSupportCrew()
        bot.llm = MagicMock()
        return bot

def test_crisis_detection(mock_crew):
    response = mock_crew.get_response("I want to end my life")
    assert response['is_crisis'] is True
    assert response['emotion'] == "crisis"

@patch('crew_bot.Crew')
def test_normal_response(MockCrew, mock_crew):
    # Mock the Crew execution result
    mock_crew_instance = MockCrew.return_value
    mock_crew_instance.kickoff.return_value = json.dumps({
        "response": "I hear you.",
        "emotion": "sad",
        "coping_suggestion": "Take a walk."
    })

    response = mock_crew.get_response("I feel sad today")
    
    assert response['is_crisis'] is False
    assert response['response'] == "I hear you."
    assert response['emotion'] == "sad"
    
def test_history_management(mock_crew):
    mock_crew.history = [
        {"role": "User", "content": "Hi"},
        {"role": "Assistant", "content": "Hello"}
    ]
    formatted = mock_crew.format_history()
    assert "User: Hi" in formatted
    assert "Assistant: Hello" in formatted

def test_reset_conversation(mock_crew):
    mock_crew.history = [{"role": "User", "content": "Hi"}]
    mock_crew.reset_conversation()
    assert len(mock_crew.history) == 0
