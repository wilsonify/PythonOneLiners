"""
## The One-Liner Recursive Quicksort Algorithm
"""


def q(l):
    """
    A Recursive Quicksort Algorithm
    :param l:
    :return:
    """
    return q([
        x for x
        in l[1:]
        if x <= l[0]
    ]
    ) + [l[0]] + q([
        x for x
        in l
        if x > l[0]
    ]
    ) if l else []


if __name__ == "__main__":
    # The Data
    unsorted = [33, 2, 3, 45, 6, 54, 33]
    # The Result
    print(q(unsorted))
    # [2, 3, 6, 33, 33, 45, 54]
