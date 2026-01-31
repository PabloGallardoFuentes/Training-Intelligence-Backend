from typing import List, Dict, Optional

def _mean(values: List[float]) -> float:
    return sum(values) / len(values)


def _interpret_ratio(ratio: Optional[float]) -> str:
    if ratio is None:
        return "insufficient data"
    if ratio < 0.8:
        return "sharp decrease"
    if ratio < 1.3:
        return "moderate increase"
    return "high increase"


def compute_load_ratio_signal(
    weekly_loads: List[int],
    acute_window: int = 4,
    chronic_window: int = 8,
) -> Dict:
    if len(weekly_loads) < chronic_window:
        return {
            "acute_load": None,
            "chronic_load": None,
            "ratio": None,
            "label": "insufficient data",
        }

    acute_slice = weekly_loads[-acute_window:]
    chronic_slice = weekly_loads[-chronic_window:]

    print(acute_slice, chronic_slice)

    acute_load = _mean(acute_slice)
    chronic_load = _mean(chronic_slice)

    if chronic_load == 0:
        ratio = None
    else:
        ratio = acute_load / chronic_load

    return {
        "acute_load": round(acute_load, 2),
        "chronic_load": round(chronic_load, 2),
        "ratio": round(ratio, 2) if ratio is not None else None,
        "label": _interpret_ratio(ratio),
    }
