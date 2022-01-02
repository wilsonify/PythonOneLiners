import pytest

from python_one_liners.machine_learning.sklearn_one_liner_08 import mvs


def test_smoke():
    print("fire?")


def test_mvs():
    # Basic Statistics in One Line

    # Dependencies
    import numpy as np

    # Stock Price Data: 5 companies
    # (row=[price_day_1, price_day_2, ...])
    x = np.array([[8, 9, 11, 12],
                  [1, 2, 2, 1],
                  [2, 8, 9, 9],
                  [9, 6, 6, 3],
                  [3, 3, 3, 3]])

    # One-liner
    avg, var, std = mvs(x)

    # Result & puzzle
    # "Averages: "
    assert avg.tolist() == [
        10., 1.5, 7., 6., 3.
    ]
    # "Variances:
    assert var.tolist() == [
        2.5, 0.25, 8.5, 4.5, 0.
    ]
    # "Standard Deviations: "
    assert std.tolist() == [
        pytest.approx(1.58113883, abs=0.1),
        pytest.approx(0.5, abs=0.1),
        pytest.approx(2.91547595, abs=0.1),
        pytest.approx(2.12132034, abs=0.1),
        pytest.approx(0, abs=0.1),
    ]
