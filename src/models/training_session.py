from dataclasses import dataclass
from datetime import date
from enum import Enum


class Sport(str, Enum):
    RUN = "run"
    BIKE = "bike"
    SWIM = "swim"

@dataclass(frozen = True)
class TrainingSession:
    id_user: int
    date: date
    sport: Sport
    duration_minutes: int
    intensity: int  # Scale RPE from 1 to 10

    def load(self) -> int:
        return self.duration_minutes * self.intensity