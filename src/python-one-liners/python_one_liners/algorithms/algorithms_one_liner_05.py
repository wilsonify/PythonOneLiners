"""
The One-Liner Calculating the Powerset by Using Functional Programming
"""

from functools import reduce  # Dependencies


def ps(sequence):
    def function(p, x):
        return p + [subset | {x} for subset in p]

    initial = [set()]
    return reduce(function, sequence, initial)


if __name__ == "__main__":
    # The Data
    s_outer = {1, 2, 3}
    # The Result
    print(ps(s_outer))
    # [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]
