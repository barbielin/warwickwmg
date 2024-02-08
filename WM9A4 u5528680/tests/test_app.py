import pytest
from flask import session, g
from app import app, get_db_connection, init_db
from flask import session, get_flashed_messages

@pytest.fixture
def client():
    app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False,
        "DATABASE": "sqlite:///:memory:",
    })

    with app.test_client() as client:
        with app.app_context():
            init_db()  # Initialize the in-memory database for tests
        yield client

@pytest.fixture
def runner(client):
    return app.test_cli_runner()

def test_register(client):
    # Test for password mismatch
    response = client.post('/register', data={
        'email': 'test2@example.com',
        'Username': 'testuser2',
        'Student ID': '1234567',
        'psw': 'password',
        'psw-repeat': 'differentpassword'
    }, follow_redirects=True)
    assert b"Passwords do not match" in response.data

    # Simulate a successful registration
    response = client.post('/register', data={
        'email': 'test@example.com',
        'Username': 'testuser',
        'Student ID': '123456',
        'psw': 'testpassword',
        'psw-repeat': 'testpassword'
    }, follow_redirects= True)
    assert b"Login", "Registration successful. Please login."in response.data

def test_login(client):
    # Assuming a user has been registered in the test_register function or you seed the test DB
    response = client.post('/login', data={
        'student_id': '123456',
        'psw': 'testpassword'
    }, follow_redirects=True)
    assert b"Login successful." in response.data

    # Test invalid login
    response = client.post('/login', data={
        'student_id': 'wrongid',
        'psw': 'wrongpassword'
    }, follow_redirects=True)
    assert b"Invalid Student ID or password." in response.data
    

def test_place_order_success(client):
    # Assuming you have a setup for a test database or mock the database calls
    response = client.post('/place_order', data={
        'student_id': 'test123',
        'coffee_type': 'Americano',
        'quantity': 1,
    }, follow_redirects=True)
    
    # Check for flash message indicating success
    flash_messages = get_flashed_messages()
    assert "show_order","Order placed successfully! Estimated waiting time is {waiting_time} minutes." in flash_messages
    
    # Verify database changes (this would require a more complex setup, possibly checking test database)

    # Check for session updates if applicable
    # assert session['some_key'] == 'expected_value'

    # Verify redirection to the correct endpoint
    assert response.request.path == '/show_order'  # Adjust '/expected_endpoint' as necessary