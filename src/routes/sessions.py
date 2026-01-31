from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoReferencedTableError

from src.repositories.orm.user import UserORM
from src.repositories.db import get_db
from src.repositories.training_session_repository import TrainingSessionRepository
from src.schemas.training_session import TrainingSessionCreate

router = APIRouter(prefix="/users/{id_user}/sessions", tags=["sessions"])

@router.post("")
def create_session(
    id_user: int,
    payload: TrainingSessionCreate,
    db: Session = Depends(get_db),
):
    repo = TrainingSessionRepository(db)

    user = db.query(UserORM).filter(UserORM.id == id_user).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User {id_user} not found"
        )
    
    repo.add_from_schema(id_user, payload)
    return JSONResponse(content={"status": "ok"}, status_code=status.HTTP_200_OK)
