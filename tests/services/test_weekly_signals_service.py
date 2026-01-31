from datetime import date

from src.services.weekly_signals_service import WeeklySignalsService
from src.models.training_session import TrainingSession, Sport
from tests.fakes.fake_training_session_repository import FakeTrainingSessionRepository


def test_weekly_signals_service_happy_path():
    sessions = [
        # Week 10
        TrainingSession(1, date(2026, 3, 2), Sport.RUN, 60, 5),   # 300
        TrainingSession(1, date(2026, 3, 3), Sport.BIKE, 90, 4),  # 360
        TrainingSession(1, date(2026, 3, 4), Sport.RUN, 40, 4),   # 160
        TrainingSession(1, date(2026, 3, 5), Sport.SWIM, 30, 3),  # 90

        # History (weeks 6–9)
        TrainingSession(1, date(2026, 2, 9), Sport.RUN, 50, 4),   # 200
        TrainingSession(1, date(2026, 2, 16), Sport.RUN, 55, 4),  # 220
        TrainingSession(1, date(2026, 2, 23), Sport.RUN, 60, 4),  # 240
        TrainingSession(1, date(2026, 3, 1), Sport.RUN, 65, 4),   # 260
    ]

    repo = FakeTrainingSessionRepository(sessions)
    service = WeeklySignalsService(repo)

    result = service.execute(user_id=1, iso_year=2026, iso_week=10)

    assert result["week"] == "2026-W10"
    assert result["weekly_load"] == 910  # 300+360+160+90

    assert "monotony" in result["signals"]
    assert "load_ratio" in result["signals"]
