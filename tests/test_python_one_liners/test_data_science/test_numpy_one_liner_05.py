"""
test for numpy_one_liner_05
"""
import numpy as np
from python_one_liners.data_science.numpy_one_liner_05 import fill_average


def test_smoke():
    """ smoke """
    print("fire?")


def test_fill_average():
    """Broadcasting, Slice Assignment, and Reshaping to Clean Every i-th Array Element"""
    # Sensor data (Mo, Tu, We, Th, Fr, Sa, Su)
    tmp = np.array([1, 2, 3, 4, 3, 4, 4, 5, 3, 3, 4, 3, 4, 6, 6, 5, 5, 5, 4, 5, 5])

    # One-liner
    tmp[6::7] = fill_average(tmp)

    # Result
    assert tmp.tolist() == [
        1,
        2,
        3,
        4,
        3,
        4,
        3,
        5,
        3,
        3,
        4,
        3,
        4,
        4,
        6,
        5,
        5,
        5,
        4,
        5,
        5,
    ]
