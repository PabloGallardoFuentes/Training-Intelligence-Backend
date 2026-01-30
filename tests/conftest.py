import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

from src.repositories.orm.base import Base
from src.models.training_session import TrainingSession, Sport
from tests.fakes.fake_training_session_repository import FakeTrainingSessionRepository

@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

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
