from datetime import date

from src.models.training_session import TrainingSession, Sport


def test_training_session_creation():
    session = TrainingSession(
        id_user=1,
        date=date(2026, 1, 20),
        sport=Sport.BIKE,
        duration_minutes=90,
        intensity=4,
    )

    assert session.id_user == 1
    assert session.date == date(2026, 1, 20)
    assert session.sport == Sport.BIKE
    assert session.duration_minutes == 90
    assert session.intensity == 4

def test_training_session_load_property():
    session = TrainingSession(
        id_user=1,
        date=date(2026, 1, 20),
        sport=Sport.RUN,
        duration_minutes=60,
        intensity=5,
    )

    assert session.load() == 300  # 60 minutes * intensity 5