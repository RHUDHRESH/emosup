import pytest
import os
from database import Database

TEST_DB = "data/test_db.sqlite"

@pytest.fixture
def db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    database = Database(TEST_DB)
    yield database
    database.close()
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

def test_create_user(db):
    user_id = db.create_user("testuser", "test@example.com", "password123", "Test User")
    assert user_id is not None
    
    # Test duplicate
    user_id_dup = db.create_user("testuser", "other@example.com", "pass", "Name")
    assert user_id_dup is None

def test_authenticate_user(db):
    db.create_user("authuser", "auth@example.com", "secretpass", "Auth User")
    
    user = db.authenticate_user("authuser", "secretpass")
    assert user is not None
    assert user['username'] == "authuser"
    
    fail = db.authenticate_user("authuser", "wrongpass")
    assert fail is None

def test_create_conversation(db):
    user_id = db.create_user("convuser", "conv@example.com", "pass", "User")
    conv_id = db.create_conversation(user_id)
    assert conv_id is not None

def test_save_and_retrieve_messages(db):
    user_id = db.create_user("msguser", "msg@example.com", "pass", "User")
    conv_id = db.create_conversation(user_id)
    
    db.save_message(conv_id, "user", "Hello", "happy", 0.5, 0.1)
    db.save_message(conv_id, "assistant", "Hi there!")
    
    history = db.get_conversation_history(conv_id)
    assert len(history) == 2
    assert history[0]['content'] == "Hello"
    assert history[1]['content'] == "Hi there!"
