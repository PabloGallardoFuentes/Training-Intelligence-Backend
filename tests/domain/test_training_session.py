from datetime import date

from src.domain.training_session import TrainingSession, Sport


def test_training_session_creation():
    session = TrainingSession(
        date=date(2026, 1, 20),
        sport=Sport.BIKE,
        duration_minutes=90,
        intensity=4,
    )

    assert session.date == date(2026, 1, 20)
    assert session.sport == Sport.BIKE
    assert session.duration_minutes == 90
    assert session.intensity == 4
