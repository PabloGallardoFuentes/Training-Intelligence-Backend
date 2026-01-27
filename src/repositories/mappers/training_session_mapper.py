from src.models.training_session import TrainingSession
from src.repositories.orm.training_session import TrainingSessionORM

def to_domain(session_orm: TrainingSessionORM) -> TrainingSession:
    return TrainingSession(
        id_user=session_orm.id_user,
        date=session_orm.date,
        sport=session_orm.sport,
        duration_minutes=session_orm.duration_minutes,
        intensity=session_orm.intensity,
    )