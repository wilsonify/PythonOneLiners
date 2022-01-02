from python_one_liners.python_tricks.quicksort import qsort


def test_smoke():
    print("fire?")


def test_q():
    assert qsort([]) == []
    assert qsort([1]) == [1]
    assert qsort([None]) == [None]
    assert qsort([10, 35, 633, 54, 1123, 0]) == [0, 10, 35, 54, 633, 1123]
