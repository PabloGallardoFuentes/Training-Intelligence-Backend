from datetime import date
from pydantic import BaseModel
from src.models.training_session import Sport

class TrainingSessionCreate(BaseModel):
    date: date
    sport: Sport
    duration_minutes: int
    intensity: int
