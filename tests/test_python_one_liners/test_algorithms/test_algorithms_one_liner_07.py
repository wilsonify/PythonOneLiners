from python_one_liners.algorithms.algorithms_one_liner_07 import primes


def test_smoke():
    print("fire?")


def test_primes():
    # Finding Prime Numbers with the Sieve of Eratosthenes
    assert primes(100) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
