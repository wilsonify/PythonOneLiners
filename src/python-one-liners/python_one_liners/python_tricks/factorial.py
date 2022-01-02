from functools import reduce


def fact(n):
    """Factorial Python One-Liner"""
    return reduce(lambda x, y: x * y, range(1, n + 1))


if __name__ == "__main__":
    # Factorial Python One-Liner
    print(fact(10))  # 3628800
