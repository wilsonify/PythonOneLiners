from python_one_liners.python_tricks.eratosthenes import Eratosthenes


def test_smoke():
    print("fire?")


def test_Eratosthenes():
    # Sieve of Eratosthenes Python One-liner
    assert Eratosthenes(100) == {
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    }
