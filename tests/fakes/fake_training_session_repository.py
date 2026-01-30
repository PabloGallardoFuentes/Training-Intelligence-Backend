from typing import List
from src.models.training_session import TrainingSession

class FakeTrainingSessionRepository:
    def __init__(self, sessions: List[TrainingSession]):
        self._sessions = sessions

    def list_by_user(self, id_user: int):
        return [s for s in self._sessions if s.id_user == id_user]

    def list_by_user_and_week(self, id_user: int, iso_year: int, iso_week: int):
        def is_in_week(session: TrainingSession) -> bool:
            session_iso_year, session_iso_week, _ = session.date.isocalendar()
            return session_iso_year == iso_year and session_iso_week == iso_week

        return [
            s
            for s in self._sessions
            if s.id_user == id_user and is_in_week(s)
        ]