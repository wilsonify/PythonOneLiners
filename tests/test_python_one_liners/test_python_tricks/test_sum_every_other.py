from python_one_liners.python_tricks.sum_every_other import sum_every_other


def test_smoke():
    print("fire?")


def test_q():
    assert sum_every_other([100, 30, 405, 303, 1000]) == 1505
