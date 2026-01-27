from collections import defaultdict
from typing import Dict

from src.models.training_session import TrainingSession

def calculate_session_load(session: TrainingSession) -> int:
    """
    Calculate the load of a training session based on its duration and intensity.

    Args:
        session (TrainingSession): The training session object containing duration and intensity.

    Returns:
        int: The calculated load of the session.
    """
    return session.duration_minutes * session.intensity

def aggregate_weekly_load(
    sessions: list[TrainingSession]
) -> Dict[str, Dict]:
    """
    Aggregates load by ISO week.

    Args:
        sessions (list[TrainingSession]): A list of training session objects.

    Returns:
        {
            "2026-W04": {
                "total": int,
                "by_sport": { "swim": int, "bike": int, "run": int }
            }
        }
    """
    weekly_data = defaultdict(lambda: {"total": 0, "by_sport": defaultdict(int)})

    for session in sessions:
        year, week, _ = session.date.isocalendar()
        week_key = f"{year}-W{week:02d}"

        load = calculate_session_load(session)
        weekly_data[week_key]["total"] += load
        weekly_data[week_key]["by_sport"][session.sport.value] += load

    return weekly_data