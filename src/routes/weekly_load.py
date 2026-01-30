from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.repositories.db import get_db
from src.repositories.training_session_repository import TrainingSessionRepository
from src.services.weekly_load_service import WeeklyLoadService

router = APIRouter(
    prefix="/users/{user_id}/weekly-load",
    tags=["weekly-load"],
)


@router.get("")
def get_weekly_load(
    user_id: int,
    year: int,
    week: int,
    db: Session = Depends(get_db),
):
    repo = TrainingSessionRepository(db)
    service = WeeklyLoadService(repo)

    return service.execute(
        id_user=user_id,
        iso_year=year,
        iso_week=week,
    )
