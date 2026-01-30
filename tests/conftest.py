# tests/conftest.py
import pytest
from datetime import date
from src.models.training_session import TrainingSession, Sport
from tests.fakes.fake_training_session_repository import FakeTrainingSessionRepository


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
