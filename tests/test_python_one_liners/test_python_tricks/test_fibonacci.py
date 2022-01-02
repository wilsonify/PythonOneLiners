from python_one_liners.algorithms.algorithms_one_liner_10 import q


def test_smoke():
    print("fire?")


def test_q():


    # Fibonacci Python One-Liner
    fib = lambda x: x if x < 2 else fib(x - 1) + fib(x - 2)