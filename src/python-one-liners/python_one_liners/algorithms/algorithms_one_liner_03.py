"""
The One-Liner Counting Permutations with Recursive Factorial Functions
"""


def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


if __name__ == "__main__":
    # The Data
    n_outer = 5
    # The Result
    print(factorial(n_outer))  # 120
