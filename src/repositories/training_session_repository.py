from sqlalchemy.orm import Session
from src.repositories.orm.training_session import TrainingSessionORM
from src.repositories.mappers.training_session_mapper import to_domain

class TrainingSessionRepository:

    def __init__(self, db: Session):
        self.db = db

    def add(self, session: TrainingSessionORM) -> None:
        self.db.add(session)

    def list_by_user(self, id_user: int):
        rows = (
            self.db.query(TrainingSessionORM)
            .filter(TrainingSessionORM.id_user == id_user)
            .all()
        )
        return [to_domain(r) for r in rows]
