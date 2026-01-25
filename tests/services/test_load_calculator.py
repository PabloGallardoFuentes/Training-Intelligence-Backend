from datetime import date

from src.domain.training_session import TrainingSession, Sport
from src.services.load_calculator import calculate_session_load, aggregate_weekly_load


def test_calculate_session_load():
    session = TrainingSession(
        date=date(2026, 1, 20),
        sport=Sport.RUN,
        duration_minutes=40,
        intensity=5,
    )

    load = calculate_session_load(session)

    assert load == 200

def test_aggregate_weekly_load_single_week():
    sessions = [
        TrainingSession(date(2026, 1, 19), Sport.SWIM, 60, 3),  # W04
        TrainingSession(date(2026, 1, 20), Sport.BIKE, 90, 4),  # W04
        TrainingSession(date(2026, 1, 21), Sport.RUN, 45, 5),   # W04
    ]

    weekly = aggregate_weekly_load(sessions)

    assert "2026-W04" in weekly
    assert weekly["2026-W04"]["total"] == (60*3 + 90*4 + 45*5)


def test_aggregate_weekly_load_by_sport():
    sessions = [
        TrainingSession(date(2026, 1, 19), Sport.BIKE, 60, 3),
        TrainingSession(date(2026, 1, 20), Sport.BIKE, 90, 4),
        TrainingSession(date(2026, 1, 21), Sport.RUN, 45, 5),
    ]

    weekly = aggregate_weekly_load(sessions)
    data = weekly["2026-W04"]["by_sport"]

    assert data["bike"] == (60*3 + 90*4)
    assert data["run"] == (45*5)

def test_sessions_in_different_weeks_are_separated():
    sessions = [
        TrainingSession(date(2026, 1, 25), Sport.BIKE, 60, 3),  # W04 (domingo)
        TrainingSession(date(2026, 1, 26), Sport.BIKE, 60, 3),  # W05 (lunes)
    ]

    weekly = aggregate_weekly_load(sessions)

    assert "2026-W04" in weekly
    assert "2026-W05" in weekly
    assert weekly["2026-W04"]["total"] == 180
    assert weekly["2026-W05"]["total"] == 180
