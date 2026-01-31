from fastapi.testclient import TestClient
from datetime import date

from main import app
from src.repositories.orm.training_session import TrainingSessionORM
from src.models.training_session import Sport


client = TestClient(app)


def test_get_weekly_load(client, db_session):
    # Arrange: datos en DB
    db_session.add_all([
        TrainingSessionORM(
            id_user=1,
            date=date(2026, 3, 4),  # week 10
            sport=Sport.RUN,
            duration_minutes=60,
            intensity=5,
        ),
        TrainingSessionORM(
            id_user=1,
            date=date(2026, 3, 5),
            sport=Sport.BIKE,
            duration_minutes=90,
            intensity=4,
        ),
    ])
    db_session.commit()

    # Act
    response = client.get(
        "/users/1/weekly-load",
        params={"year": 2026, "week": 10},
    )

    # Assert
    assert response.status_code == 200

    body = response.json()
    assert body["total_load"] == 60 * 5 + 90 * 4
    assert body["load_by_sport"]["run"] == 300
    assert body["load_by_sport"]["bike"] == 360