from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.repositories.orm.base import Base

DATABASE_URL = "sqlite:///./dev.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
