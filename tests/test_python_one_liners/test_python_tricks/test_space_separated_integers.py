from python_one_liners.python_tricks.space_separated_integers import spi


def test_smoke():
    print("fire?")


def test_q():
    lis = spi("10 50 400 340")
    assert lis == [10, 50, 400, 340]
