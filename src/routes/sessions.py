from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.repositories.db import get_db
from src.repositories.training_session_repository import TrainingSessionRepository
from src.schemas.training_session import TrainingSessionCreate

router = APIRouter(prefix="/users/{user_id}/sessions", tags=["sessions"])

@router.post("")
def create_session(
    user_id: int,
    payload: TrainingSessionCreate,
    db: Session = Depends(get_db),
):
    repo = TrainingSessionRepository(db)
    repo.add_from_schema(user_id, payload)
    return {"status": "ok"}
