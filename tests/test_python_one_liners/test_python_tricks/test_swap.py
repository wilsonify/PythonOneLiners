from python_one_liners.python_tricks.swap import swaparoo


def test_smoke():
    print("fire?")


def test_q():
    a = 100
    b = 2000
    a, b = swaparoo(a, b)
    assert a == 2000
    assert b == 100
