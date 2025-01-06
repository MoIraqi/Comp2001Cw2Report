import pytest
from app import app, db


@pytest.fixture
def client():
    # Set up the test client with the application context
    with app.test_client() as client:
        with app.app_context():  # Ensure the app context is pushed
            db.create_all()  # Ensure the DB tables are created for testing
            yield client
            db.session.remove()  # Clean up after each test
            db.drop_all()  # Drop tables after the test to ensure isolation


def test_connection(client):
    # Simulate a GET request to the /api/test_connection route
    response = client.get('/api/test_connection')

    # Check the response status code and message
    if response.status_code == 200:
        assert response.json["message"] == "Connection successful"
    else:
        assert response.status_code == 500
        assert "Database connection failed" in response.json["error"]
