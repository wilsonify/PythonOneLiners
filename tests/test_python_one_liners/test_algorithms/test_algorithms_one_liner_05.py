from python_one_liners.algorithms.algorithms_one_liner_05 import ps


def test_smoke():
    print("fire?")


def test_powerset():
    # Calculating the Powerset by Using Functional Programming
    s = {1, 2, 3}
    assert ps(s) == [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]
