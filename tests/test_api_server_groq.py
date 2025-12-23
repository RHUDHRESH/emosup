import pytest
import json
from api_server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check_endpoint(client):
    """Test the /api/health endpoint."""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy' or data['status'] == 'degraded'
    assert 'groq' in data
    assert 'chatbot' in data

def test_flight_check_endpoint(client):
    """Test the /api/flight-check endpoint."""
    response = client.get('/api/flight-check')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'services' in data
    assert 'groq' in data['services']
    assert 'api_server' in data['services']
