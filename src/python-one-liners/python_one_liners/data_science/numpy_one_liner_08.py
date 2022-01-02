# How to Create Advanced Array Filters with Statistics, Math, and Logic
import numpy as np


def find_outliers(a):
    """
    find all outlier days for which the statistics deviate
    more than the standard deviation from their mean statistics.
    :return:
    """
    mean, stdev = np.mean(a, axis=0), np.std(a, axis=0)
    # [811.2 76.4 88. ], [152.97764543 6.85857128 29.04479299]

    # One-liner
    outliers = (
        (np.abs(a[:, 0] - mean[0]) > stdev[0])
        * (np.abs(a[:, 1] - mean[1]) > stdev[1])
        * (np.abs(a[:, 2] - mean[2]) > stdev[2])
    )
    return a[outliers]


if __name__ == "__main__":
    # Dependencies

    # Website analytics data:
    # (row = day), (col = users, bounce, duration)
    a_outer = np.array(
        [[815, 70, 115], [767, 80, 50], [912, 74, 77], [554, 88, 70], [1008, 65, 128]]
    )
    result = find_outliers(a_outer)
    # Result
    print(result)
    """
    [[1008   65  128]]
    """
