"""
test for LinearRegression
"""

from python_one_liners.data_science.numpy_one_liner_10 import find_most_copurchased


def test_smoke():
    """ smoke """
    print("fire?")


def test_LinearRegression(basket):
    # Linear Regression


    ## Dependencies
    from sklearn.linear_model import LinearRegression
    import numpy as np

    ## Data (Apple stock prices)
    apple = np.array([155, 156, 157])
    n = len(apple)

    ## One-liner
    model = LinearRegression().fit(np.arange(n).reshape((n,1)), apple)

    ## Result & puzzle
    print(model.predict([[3],[4]]))
    '''
    [158. 159.]
    '''
