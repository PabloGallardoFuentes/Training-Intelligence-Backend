from datetime import date

from src.repositories.orm.training_session import TrainingSessionORM
from src.models.training_session import Sport


def test_get_weekly_signals(client, db_session):
    # Arrange: datos históricos + semana actual
    db_session.add_all([
        # Week 10 (target)
        TrainingSessionORM(
            id_user=1,
            date=date(2026, 3, 2),
            sport=Sport.RUN,
            duration_minutes=60,
            intensity=5,   # 300
        ),
        TrainingSessionORM(
            id_user=1,
            date=date(2026, 3, 3),
            sport=Sport.BIKE,
            duration_minutes=90,
            intensity=4,   # 360
        ),
        TrainingSessionORM(
            id_user=1,
            date=date(2026, 3, 4),
            sport=Sport.RUN,
            duration_minutes=40,
            intensity=4,   # 160
        ),
        TrainingSessionORM(
            id_user=1,
            date=date(2026, 3, 5),
            sport=Sport.SWIM,
            duration_minutes=30,
            intensity=3,   # 90
        ),

        # History weeks (6–9)
        TrainingSessionORM(
            id_user=1,
            date=date(2026, 2, 9),
            sport=Sport.RUN,
            duration_minutes=50,
            intensity=4,   # 200
        ),
        TrainingSessionORM(
            id_user=1,
            date=date(2026, 2, 16),
            sport=Sport.RUN,
            duration_minutes=55,
            intensity=4,   # 220
        ),
        TrainingSessionORM(
            id_user=1,
            date=date(2026, 2, 23),
            sport=Sport.RUN,
            duration_minutes=60,
            intensity=4,   # 240
        ),
        TrainingSessionORM(
            id_user=1,
            date=date(2026, 3, 1),
            sport=Sport.RUN,
            duration_minutes=65,
            intensity=4,   # 260
        ),
    ])
    db_session.commit()

    # Act
    response = client.get(
        "/users/1/signals",
        params={"year": 2026, "week": 10},
    )

    # Assert
    assert response.status_code == 200

    body = response.json()

    assert body["week"] == "2026-W10"
    assert body["weekly_load"] == 910

    signals = body["signals"]

    assert "monotony" in signals
    assert "load_ratio" in signals

    assert signals["monotony"]["label"] in {
        "low monotony",
        "moderate monotony",
        "high monotony",
        "insufficient data",
    }
    print(signals["load_ratio"])
    assert signals["load_ratio"]["ratio"] is None
