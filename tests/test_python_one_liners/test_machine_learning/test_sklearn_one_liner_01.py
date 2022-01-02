"""
test for sklearn_one_liner_01
"""
from python_one_liners.machine_learning.sklearn_one_liner_01 import myline


def test_smoke():
    """ smoke """
    print("fire?")


def test_LinearRegression():
    # Linear Regression

    # Dependencies
    import numpy as np

    # Data (Apple stock prices)
    apple = np.array([155, 156, 157])
    n = len(apple)

    # One-liner
    model = myline(apple)

    # Result & puzzle
    assert model.predict([[3], [4]]).tolist() == [158.0, 159.0]
