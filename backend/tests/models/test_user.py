from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from api.dependencies import get_db
from main import app


client = TestClient(app)


def test_create_user(db: Session):
    user = {"username": "testuser", "email": "testuser@example.com", "password": "testpassword"}
    response = client.post("/users/", json=user)
    assert response.status_code == 200
    assert response.json()["username"] == user["username"]
    assert response.json()["email"] == user["email"]