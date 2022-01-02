from python_one_liners.algorithms.algorithms_one_liner_10 import q


def test_smoke():
    print("fire?")


def test_q():
    # A Recursive Quicksort Algorithm
    unsorted = [33, 2, 3, 45, 6, 54, 33]
    assert q(unsorted) == [2, 3, 6, 33, 33, 45, 54]
