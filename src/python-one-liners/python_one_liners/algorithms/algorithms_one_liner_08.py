"""
The One-Liner Calculating the Fibonacci Series using reduce()
"""

from functools import reduce  # Dependencies


def fibs(n=10):
    def function(x, _):
        return x + [x[-2] + x[-1]]

    sequence = [0] * (n - 2)
    initial = [0, 1]
    return reduce(function, sequence, initial)


if __name__ == "__main__":
    # The Data
    n_outer = 10
    # The Result
    print(fibs(n_outer))
    '''
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    '''
