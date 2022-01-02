from python_one_liners.algorithms.algorithms_one_liner_09 import bs, bs_ml


def test_smoke():
    print("fire?")


def test_bs():
    # A Recursive Binary Search Algorithm
    l = [3, 6, 14, 16, 33, 55, 56, 89]
    x = 33
    assert bs(l, x, 0, len(l) - 1) == 4


def test_bs_ml():
    l = [3, 6, 14, 16, 33, 55, 56, 89]
    x = 33
    assert bs_ml(l, x, 0, len(l) - 1) == 4
