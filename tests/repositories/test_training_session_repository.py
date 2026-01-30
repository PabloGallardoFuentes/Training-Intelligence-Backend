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
def repository(db_session):
    return TrainingSessionRepository(db_session)

def test_add_and_list_by_user(repository, db_session):
    # Add a user
    db_session.add(UserORM(id=1))
    db_session.commit()

    # Add a session
    session_orm = TrainingSessionORM(
        id_user=1,
        date=date(2026, 1, 20),
        sport=Sport.BIKE,
        duration_minutes=90,
        intensity=4,
    )
    repository.add(session_orm)
    db_session.commit()
    # List by user
    result = repository.list_by_user(1)
    assert len(result) == 1
    assert result[0].id_user == 1
    assert result[0].sport == Sport.BIKE
    assert result[0].duration_minutes == 90
    assert result[0].intensity == 4

def test_list_by_user_and_week(repository, db_session):
    # Add a user
    db_session.add(UserORM(id=1))
    db_session.commit()

    # Add sessions
    sessions = [
        TrainingSessionORM(
            id_user=1,
            date=date(2026, 3, 4),  # Wednesday
            sport=Sport.RUN,
            duration_minutes=60,
            intensity=5,
        ),
        TrainingSessionORM(
            id_user=1,
            date=date(2026, 3, 5),  # Thursday
            sport=Sport.BIKE,
            duration_minutes=90,
            intensity=4,
        ),
        TrainingSessionORM(
            id_user=1,
            date=date(2026, 3, 15),  # Next week Monday
            sport=Sport.SWIM,
            duration_minutes=30,
            intensity=6,
        ),
    ]
    for s in sessions:
        repository.add(s)
    db_session.commit()

    # List by user and week (ISO week 10 of 2026)
    result = repository.list_by_user_and_week(1, 2026, 10)
    assert len(result) == 2
    dates = {r.date for r in result}
    assert date(2026, 3, 4) in dates
    assert date(2026, 3, 5) in dates

def test_empty_week_returns_empty_list(db_session):
    repo = TrainingSessionRepository(db_session)

    sessions = repo.list_by_user_and_week(
        id_user=1,
        iso_year=2026,
        iso_week=1,
    )

    assert sessions == []

def test_add_from_schema(repository, db_session):
    schema = TrainingSessionCreate(
        date=date(2026, 1, 21),
        sport=Sport.RUN,
        duration_minutes=60,
        intensity=5,
    )
    repository.add_from_schema(2, schema)
    db_session.commit()
    # List by user
    result = repository.list_by_user(2)
    assert len(result) == 1
    assert result[0].id_user == 2
    assert result[0].sport == Sport.RUN
    assert result[0].duration_minutes == 60
    assert result[0].intensity == 5

def test_list_by_user_empty(repository, db_session):
    result = repository.list_by_user(999)
    assert result == []
