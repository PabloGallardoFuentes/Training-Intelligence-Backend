from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.repositories.db import get_db
from src.repositories.training_session_repository import TrainingSessionRepository
from src.services.weekly_signals_service import WeeklySignalsService

router = APIRouter(
    prefix="/users/{id_user}/signals",
    tags=["signals"],
)


@router.get("")
def get_weekly_signals(
    id_user: int,
    year: int,
    week: int,
    db: Session = Depends(get_db),
):
    repo = TrainingSessionRepository(db)
    service = WeeklySignalsService(repo)

    return service.execute(
        user_id=id_user,
        iso_year=year,
        iso_week=week,
    )
