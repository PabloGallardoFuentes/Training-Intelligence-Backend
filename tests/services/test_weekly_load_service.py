from datetime import date

from src.models.training_session import Sport, TrainingSession
from src.services.weekly_load_service import WeeklyLoadService


def test_weekly_load_aggregation(weekly_repo):
    service = WeeklyLoadService(weekly_repo)
    result = service.execute(id_user=1, iso_year=2026, iso_week=10)
    
    assert result["total_load"] == 60 * 5 + 90 * 4
    assert result["load_by_sport"][Sport.RUN] == 300
