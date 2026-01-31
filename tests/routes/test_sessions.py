from fastapi.testclient import TestClient
from datetime import date
import pytest

from main import app
from src.repositories.orm.base import Base
from src.repositories.orm.user import UserORM
from src.repositories.db import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def test_create_session_success(client, db_session):
    # Arrange: crear usuario
    user = UserORM(id=1)
    db_session.add(user)
    db_session.commit()
    payload = {
        "date": "2026-03-04",
        "sport": "run",
        "duration_minutes": 60,
        "intensity": 5
    }
    response = client.post("/users/1/sessions", json=payload)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_session_user_not_found(client, db_session):
    payload = {
        "date": "2026-03-04",
        "sport": "run",
        "duration_minutes": 60,
        "intensity": 5
    }
    response = client.post("/users/999/sessions", json=payload)

    print(response.json())
    assert response.status_code == 404
    assert response.json()["detail"] == "User 999 not found"
