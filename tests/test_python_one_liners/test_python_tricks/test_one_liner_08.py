from python_one_liners.python_tricks.one_liner_08 import clean_cycle


def test_smoke():
    print("fire?")


def test_q():
    # Analyzing Cardiac Health Data with List Concatenation

    # Dependencies

    # Data
    cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

    # One-Liner
    expected_cycles = clean_cycle(cardiac_cycle)

    assert expected_cycles == [
        60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62,
        64, 68, 77, 80, 76, 71, 66, 61, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62, 64, 68,
        77, 80, 76, 71, 66, 61, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62, 64, 68, 77, 80,
        76, 71, 66, 61, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62, 64, 68, 77, 80, 76, 71,
        66, 61, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61
    ]
