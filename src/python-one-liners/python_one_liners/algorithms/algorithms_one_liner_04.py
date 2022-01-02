"""
The One-Liner Finding the Levenshtein Distance
"""


def ls(a, b):
    """
    Levenshtein Distance
    :param a:
    :param b:
    :return:
    """
    return len(b) \
        if not a \
        else len(a) \
        if not b \
        else min(
        ls(a[1:], b[1:]) + (a[0] != b[0]),
        ls(a[1:], b) + 1,
        ls(a, b[1:]) + 1
    )


def ls_ml(a, b):
    """
    Levenshtein Distance
    :param a:
    :param b:
    :return:
    """
    if not a:
        return len(b)
    if not b:
        return len(a)
    return min(
        ls_ml(a[1:], b[1:]) + (a[0] != b[0]),
        ls_ml(a[1:], b) + 1,
        ls_ml(a, b[1:]) + 1
    )


if __name__ == "__main__":
    # The Data
    a_outer = "cat"
    b_outer = "chello"
    c_outer = "chess"
    # The Result
    print(ls(a_outer, b_outer))  # 5
    print(ls(a_outer, c_outer))  # 4
    print(ls(b_outer, c_outer))  # 3
