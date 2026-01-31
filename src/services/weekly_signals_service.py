from collections import defaultdict
from datetime import date

from src.services.load_calculator import calculate_session_load
from src.services.signals.monotony import compute_monotony_signal
from src.services.signals.load_ratio import compute_load_ratio_signal


class WeeklySignalsService:
    def __init__(self, training_session_repository):
        self.repo = training_session_repository

    def execute(self, user_id: int, iso_year: int, iso_week: int) -> dict:
        sessions = self.repo.list_by_user(user_id)

        # 1️⃣ Daily loads
        daily_loads_by_date = defaultdict(int)
        for s in sessions:
            daily_loads_by_date[s.date] += calculate_session_load(s)

        # 2️⃣ Weekly loads (history)
        weekly_loads = defaultdict(int)
        for day, load in daily_loads_by_date.items():
            year, week, _ = day.isocalendar()
            weekly_loads[(year, week)] += load

        # 3️⃣ Target week
        week_key = (iso_year, iso_week)
        weekly_load = weekly_loads.get(week_key, 0)

        # 4️⃣ Historical weekly loads (sorted)
        sorted_weeks = sorted(weekly_loads.keys())
        weekly_load_series = [
            weekly_loads[w] for w in sorted_weeks if w <= week_key
        ]

        # 5️⃣ Signals
        daily_loads_current_week = [
            load for day, load in daily_loads_by_date.items()
            if day.isocalendar()[:2] == week_key
        ]

        monotony = compute_monotony_signal(daily_loads_current_week)
        load_ratio = compute_load_ratio_signal(weekly_load_series)

        return {
            "week": f"{iso_year}-W{iso_week:02d}",
            "weekly_load": weekly_load,
            "signals": {
                "monotony": monotony,
                "load_ratio": load_ratio,
            },
        }
