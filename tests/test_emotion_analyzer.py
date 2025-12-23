import pytest
from emotion_analyzer import EmotionAnalyzer

@pytest.fixture
def analyzer():
    return EmotionAnalyzer()

def test_analyze_sentiment_positive(analyzer):
    text = "I am so happy and excited!"
    result = analyzer.analyze_sentiment(text)
    assert result['polarity'] > 0

def test_analyze_sentiment_negative(analyzer):
    text = "I am feeling terrible and sad."
    result = analyzer.analyze_sentiment(text)
    assert result['polarity'] < 0

def test_detect_emotions_happy(analyzer):
    text = "I am full of joy and happiness"
    emotions = analyzer.detect_emotions(text)
    assert emotions[0][0] == "happy"

def test_detect_emotions_sad(analyzer):
    text = "I feel down and depressed"
    emotions = analyzer.detect_emotions(text)
    assert emotions[0][0] == "sad"

def test_get_primary_emotion_fallback(analyzer):
    # Text with no keywords, relying on sentiment
    text = "This is simply wonderful."
    emotion = analyzer.get_primary_emotion(text)
    assert emotion == "happy"

def test_coping_suggestion(analyzer):
    suggestion = analyzer.get_coping_suggestion("sad")
    assert isinstance(suggestion, str)
    assert len(suggestion) > 0
