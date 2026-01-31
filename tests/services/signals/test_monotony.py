from src.services.signals.monotony import compute_monotony_signal

def test_monotony_signal_normal_week():
    daily_loads = [100, 200, 300, 400]

    signal = compute_monotony_signal(daily_loads)

    assert signal["value"] is not None
    assert signal["label"] == "moderate monotony"

def test_monotony_signal_constant_load():
    daily_loads = [200, 200, 200, 200]

    signal = compute_monotony_signal(daily_loads)

    assert signal["value"] is None
    assert signal["label"] == "insufficient data"

def test_monotony_signal_single_day():
    signal = compute_monotony_signal([300])

    assert signal["value"] is None

def test_monotony_signal_empty():
    signal = compute_monotony_signal([])

    assert signal["label"] == "insufficient data"
