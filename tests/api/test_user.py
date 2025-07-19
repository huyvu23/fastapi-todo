from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login_success():
    response = client.post("/api/v1/auth/login", json={"username": "dominik", "password": "12345678"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

def test_login_fail_invalid_user():
    response = client.post("/api/v1/auth/login", json={"username": "dominik", "password": "secret"})
    assert response.status_code == 401
    assert "Invalid" in response.json()["detail"]
