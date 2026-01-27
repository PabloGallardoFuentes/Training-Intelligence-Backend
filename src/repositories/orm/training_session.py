from sqlalchemy import ForeignKey, Integer, Date, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.repositories.orm.base import Base
from src.models.training_session import Sport


class TrainingSessionORM(Base):
    __tablename__ = "training_session"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("user.id"))

    date: Mapped[Date] = mapped_column(Date)
    sport: Mapped[Sport] = mapped_column(Enum(Sport))
    duration_minutes: Mapped[int] = mapped_column(Integer)
    intensity: Mapped[int] = mapped_column(Integer)  # Scale RPE from 1 to 10
