"""
The One-Liner Recursive Binary Search Algorithm
"""


def bs(l, x, lo, hi):
    """
    A Recursive Binary Search Algorithm
    :param l:
    :param x:
    :param lo:
    :param hi:
    :return:
    """
    return -1 \
        if lo > hi \
        else (lo + hi) // 2 \
        if l[(lo + hi) // 2] == x \
        else bs(l, x, lo, (lo + hi) // 2 - 1) \
        if l[(lo + hi) // 2] > x \
        else bs(l, x, (lo + hi) // 2 + 1, hi)


def bs_ml(l, x, lo, hi):
    """
    Multi-Line
    A Recursive Binary Search Algorithm
    :param l:
    :param x:
    :param lo:
    :param hi:
    :return:
    """
    if lo > hi:
        return -1
    if l[(lo + hi) // 2] == x:
        return (lo + hi) // 2
    if l[(lo + hi) // 2] > x:
        return bs(l, x, lo, (lo + hi) // 2 - 1)
    return bs(l, x, (lo + hi) // 2 + 1, hi)


if __name__ == "__main__":
    # The Data
    l_outer = [3, 6, 14, 16, 33, 55, 56, 89]
    x_outer = 33
    # The Results
    print(bs(l_outer, x_outer, 0, len(l_outer) - 1))
    # 4
