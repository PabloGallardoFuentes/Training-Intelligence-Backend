import json
from datetime import datetime
from pathlib import Path

from src.domain.training_session import TrainingSession, Sport
from src.services.load_calculator import aggregate_weekly_load


DATA_PATH = Path("data/sessions.json")


def load_sessions() -> list[TrainingSession]:
    with open(DATA_PATH, "r") as f:
        raw_sessions = json.load(f)

    sessions = []
    for item in raw_sessions:
        sessions.append(
            TrainingSession(
                date=datetime.fromisoformat(item["date"]).date(),
                sport=Sport(item["sport"]),
                duration_minutes=item["duration_minutes"],
                intensity=item["intensity"],
            )
        )
    return sessions


def print_weekly_report(weekly_data: dict) -> None:
    for week, data in sorted(weekly_data.items()):
        print(f"\nWeek {week}")
        print(f"Total load: {data['total']}")

        for sport, load in data["by_sport"].items():
            print(f"{sport.capitalize()}: {load}")


def main():
    sessions = load_sessions()
    weekly_data = aggregate_weekly_load(sessions)
    print_weekly_report(weekly_data)


if __name__ == "__main__":
    main()
