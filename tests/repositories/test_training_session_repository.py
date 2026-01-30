import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.repositories.orm.user import UserORM
from src.repositories.orm.base import Base
from src.repositories.orm.training_session import TrainingSessionORM
from src.repositories.training_session_repository import TrainingSessionRepository
from src.schemas.training_session import TrainingSessionCreate
from datetime import date
from src.models.training_session import Sport

@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    db = Session()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def repository(in_memory_db):
    return TrainingSessionRepository(in_memory_db)

def test_add_and_list_by_user(repository, in_memory_db):
    # Add a user
    in_memory_db.add(UserORM(id=1))
    in_memory_db.commit()
    
    # Add a session
    session_orm = TrainingSessionORM(
        id_user=1,
        date=date(2026, 1, 20),
        sport=Sport.BIKE,
        duration_minutes=90,
        intensity=4,
    )
    repository.add(session_orm)
    in_memory_db.commit()
    # List by user
    result = repository.list_by_user(1)
    assert len(result) == 1
    assert result[0].id_user == 1
    assert result[0].sport == Sport.BIKE
    assert result[0].duration_minutes == 90
    assert result[0].intensity == 4

def test_add_from_schema(repository, in_memory_db):
    schema = TrainingSessionCreate(
        date=date(2026, 1, 21),
        sport=Sport.RUN,
        duration_minutes=60,
        intensity=5,
    )
    repository.add_from_schema(2, schema)
    # List by user
    result = repository.list_by_user(2)
    assert len(result) == 1
    assert result[0].id_user == 2
    assert result[0].sport == Sport.RUN
    assert result[0].duration_minutes == 60
    assert result[0].intensity == 5

def test_list_by_user_empty(repository):
    result = repository.list_by_user(999)
    assert result == []
