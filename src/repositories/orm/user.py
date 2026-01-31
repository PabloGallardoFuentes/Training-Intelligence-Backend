from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.repositories.orm.base import Base


class UserORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)