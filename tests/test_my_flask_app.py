import pytest
from my_flask_app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_exiting_user(client):
    response = client.get("/api/users/user_1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["username"] == "user_1"
    assert data["data"]["name"] == "Alice"
    assert data["data"]["role"] == "admin"


def test_get_nonexisting_user(client):
    response = client.get("/api/users/user_3")
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data
