from datetime import date
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
    
    def list_by_user_and_week(
        self,
        id_user: int,
        iso_year: int,
        iso_week: int,
    ):
        start_date = date.fromisocalendar(iso_year, iso_week, 1)
        end_date = date.fromisocalendar(iso_year, iso_week, 7)

        rows = (
            self.db.query(TrainingSessionORM)
            .filter(TrainingSessionORM.id_user == id_user,
                    TrainingSessionORM.date >= start_date,
                    TrainingSessionORM.date <= end_date
            )
            .all()
        )
        
        return [to_domain(r) for r in rows]
    
    def add_from_schema(self, id_user: int, schema) -> None:
        session_orm = TrainingSessionORM(
            id_user=id_user,
            date=schema.date,
            sport=schema.sport,
            duration_minutes=schema.duration_minutes,
            intensity=schema.intensity,
        )
        self.db.add(session_orm)
        self.db.commit()