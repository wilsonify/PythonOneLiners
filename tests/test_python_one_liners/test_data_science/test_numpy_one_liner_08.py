"""
test for numpy_one_liner_08
"""
import numpy as np

from python_one_liners.data_science.numpy_one_liner_08 import find_outliers


def test_smoke():
    """ smoke """
    print("fire?")


def test_find_outliers():
    """ How to Create Advanced Array Filters with Statistics, Math, and Logic """
    # Website analytics data:
    # (row = day), (col = users, bounce, duration)
    a = np.array(
        [[815, 70, 115], [767, 80, 50], [912, 74, 77], [554, 88, 70], [1008, 65, 128]]
    )

    result = find_outliers(a)
    assert result.tolist() == [[1008, 65, 128]]
