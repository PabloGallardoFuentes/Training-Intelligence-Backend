import math
from typing import List, Optional, Dict

def _compute_monotony_value(daily_loads: List[int]) -> Optional[float]:
    if len(daily_loads) < 2:
        return None

    mean = sum(daily_loads) / len(daily_loads)
    variance = sum((x - mean) ** 2 for x in daily_loads) / len(daily_loads)
    std = math.sqrt(variance)

    if std == 0:
        return None

    return mean / std


def _interpret_monotony(value: Optional[float]) -> str:
    if value is None:
        return "insufficient data"
    if value < 1.5:
        return "low monotony"
    if value < 2.5:
        return "moderate monotony"
    return "high monotony"


def compute_monotony_signal(daily_loads: List[int]) -> Dict:
    value = _compute_monotony_value(daily_loads)

    return {
        "value": round(value, 2) if value is not None else None,
        "label": _interpret_monotony(value),
        "description": _describe_monotony(value),
    }


def _describe_monotony(value: Optional[float]) -> str:
    if value is None:
        return "Not enough variability data to assess training monotony."
    if value < 1.5:
        return "Training load varies well across the week."
    if value < 2.5:
        return "Training shows moderate day-to-day repetition."
    return "Training load is highly repetitive and may increase fatigue risk."
