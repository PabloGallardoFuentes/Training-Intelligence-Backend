from fastapi.testclient import TestClient
import pytest
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

from src.repositories.orm.base import Base
from src.models.training_session import TrainingSession, Sport
from tests.fakes.fake_training_session_repository import FakeTrainingSessionRepository

@pytest.fixture
def db_session():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture
def client(db_session):
    from src.main import app
    from src.repositories.db import get_db

    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()

@pytest.fixture
def weekly_repo():
    return FakeTrainingSessionRepository(
        sessions=[
            TrainingSession(
                id_user=1,
                date=date(2026, 3, 4),
                sport=Sport.RUN,
                duration_minutes=60,
                intensity=5,
            ),
            TrainingSession(
                id_user=1,
                date=date(2026, 3, 5),
                sport=Sport.BIKE,
                duration_minutes=90,
                intensity=4,
            ),
        ]
    )
