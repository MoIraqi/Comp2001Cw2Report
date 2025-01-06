import pytest
import json
from app import app, db, Trail  # Import the app and db models


@pytest.fixture
def client():
    # Set up the test client with the application context
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables

            # Insert a sample trail for testing purposes
            sample_trail = Trail(trail_name = 'Sample Trail', description = 'A test trail')
            db.session.add(sample_trail)
            db.session.commit()

            # Simulate the authorization token (replace with your actual method for generating a token)
            token = 'YOUR_VALID_TOKEN'  # You should replace this with a valid token generation logic

            yield client, token  # Return the client and token for testing purposes

            db.session.remove()
            db.drop_all()  # Clean up the database after tests


def test_create_trail(client):
    """Test POST /api/trails"""
    client, token = client  # Unpack the client and token
    new_trail = {
        'trail_name': 'New Trail',
        'description': 'A description for a new trail'
    }
    response = client.post('/api/trails', data = json.dumps(new_trail),
                           content_type = 'application/json',
                           headers = {'Authorization': f'Bearer {token}'})
    assert response.status_code == 201  # Ensure the status code is 201 Created


def test_delete_trail(client):
    """Test DELETE /api/trails/<int:trail_id>"""
    client, token = client  # Unpack the client and token
    trail_id = 1  # Use an existing trail ID (ensure it exists in the DB)
    response = client.delete(f'/api/trails/{trail_id}', headers = {'Authorization': f'Bearer {token}'})
    assert response.status_code == 200  # Ensure the status code is 200 OK


def test_get_all_trails(client):
    """Test GET /api/trails"""
    client, token = client  # Unpack the client and token
    response = client.get('/api/trails', headers = {'Authorization': f'Bearer {token}'})
    assert response.status_code == 200  # Ensure the status code is 200 OK


def test_get_trail_by_id(client):
    """Test GET /api/trails/<int:trail_id>"""
    client, token = client  # Unpack the client and token
    trail_id = 1  # Ensure this ID exists in the DB
    response = client.get(f'/api/trails/{trail_id}', headers = {'Authorization': f'Bearer {token}'})
    assert response.status_code == 200  # Ensure the status code is 200 OK


def test_update_trail(client):
    """Test PUT /api/trails/<int:trail_id>"""
    client, token = client  # Unpack the client and token
    trail_id = 1  # Ensure this ID exists in the DB
    updated_data = {
        'trail_name': 'Updated Trail',
        'description': 'Updated description'
    }
    response = client.put(f'/api/trails/{trail_id}', data = json.dumps(updated_data),
                          content_type = 'application/json',
                          headers = {'Authorization': f'Bearer {token}'})
    assert response.status_code == 200  # Ensure the status code is 200 OK
