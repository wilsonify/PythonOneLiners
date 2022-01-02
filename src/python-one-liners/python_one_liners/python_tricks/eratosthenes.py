from functools import reduce


def Eratosthenes(n):
    return reduce(
        (lambda r, x: r - set(range(x ** 2, n, x)) if (x in r) else r),
        range(2, int(n ** 0.5)),
        set(range(2, n))
    )
if __name__ == "__main__":
    # Sieve of Eratosthenes Python One-liner
    Eratosthenes(100)