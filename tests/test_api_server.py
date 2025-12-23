import pytest
from api_server import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    rv = client.get('/api/health')
    assert rv.status_code == 200
    data = json.loads(rv.data)
    assert 'status' in data

def test_flight_check(client):
    rv = client.get('/api/flight-check')
    assert rv.status_code == 200
    data = json.loads(rv.data)
    assert 'services' in data

def test_chat_no_message(client):
    rv = client.post('/api/chat', json={})
    assert rv.status_code == 400
