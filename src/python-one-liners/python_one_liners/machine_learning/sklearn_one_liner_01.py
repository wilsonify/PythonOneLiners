# Linear Regression


import numpy as np
from sklearn.linear_model import LinearRegression


def myline(apple):
    n = len(apple)
    return LinearRegression().fit(np.arange(n).reshape((n, 1)), apple)


if __name__ == "__main__":
    ## Data (Apple stock prices)
    apple = np.array([155, 156, 157])

    ## One-liner
    model = myline(apple)

    ## Result & puzzle
    print(model.predict([[3], [4]]))
    '''
    [158. 159.]
    '''
