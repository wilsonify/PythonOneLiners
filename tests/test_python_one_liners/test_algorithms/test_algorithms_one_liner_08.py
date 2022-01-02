from python_one_liners.algorithms.algorithms_one_liner_08 import fibs


def test_smoke():
    print("fire?")


def test_fibs():
    # Calculating the Fibonacci Series with the reduce() Function
    assert fibs(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
