from collections import defaultdict
from typing import Dict

from src.repositories.training_session_repository import TrainingSessionRepository


class WeeklyLoadService:
    def __init__(self, training_session_repository: TrainingSessionRepository):
        self.training_session_repository = training_session_repository

    def execute(
        self,
        id_user: int,
        iso_year: int,
        iso_week: int,
    ) -> Dict:
        sessions = self.training_session_repository.list_by_user_and_week(
            id_user=id_user,
            iso_year=iso_year,
            iso_week=iso_week,
        )

        total_load = 0
        load_by_sport = defaultdict(int)

        for session in sessions:
            session_load = session.duration_minutes * session.intensity
            total_load += session_load
            load_by_sport[session.sport] += session_load

        return {
            "iso_year": iso_year,
            "iso_week": iso_week,
            "total_load": total_load,
            "load_by_sport": dict(load_by_sport),
        }