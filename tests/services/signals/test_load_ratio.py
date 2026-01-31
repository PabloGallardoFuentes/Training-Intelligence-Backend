from src.services.signals.load_ratio import compute_load_ratio_signal

def test_load_ratio_normal_case():
    weekly_loads = [300, 320, 340, 360, 380, 400, 420, 440]
    # last week = 440

    signal = compute_load_ratio_signal(
        weekly_loads=weekly_loads,
        acute_window=4,
        chronic_window=8,
    )

    assert round(signal["acute_load"], 1) == 410.0
    assert round(signal["chronic_load"], 1) == 370.0
    assert round(signal["ratio"], 2) == round(410 / 370, 2)
    assert signal["label"] == "moderate increase"

def test_load_ratio_insufficient_data():
    weekly_loads = [300, 320, 340]

    signal = compute_load_ratio_signal(weekly_loads)

    assert signal["ratio"] is None
    assert signal["label"] == "insufficient data"

def test_load_ratio_zero_chronic():
    weekly_loads = [0, 0, 0, 0, 0, 0, 0, 0]

    signal = compute_load_ratio_signal(weekly_loads)

    assert signal["ratio"] is None
