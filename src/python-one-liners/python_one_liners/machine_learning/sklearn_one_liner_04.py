# K-Nearest Neighbors in One Line


import numpy as np
## Dependencies
from sklearn.neighbors import KNeighborsRegressor


def myknn(X):
    return KNeighborsRegressor(n_neighbors=3).fit(X[:, 0].reshape(-1, 1), X[:, 1])


if __name__ == "__main__":
    ## Data (House Size (square meters) / House Price ($))
    X = np.array([[35, 30000], [45, 45000], [40, 50000],
                  [35, 35000], [25, 32500], [40, 40000]])

    ## One-liner
    KNN = myknn(X)

    ## Result & puzzle
    res = KNN.predict([[30]])
    print(res)
    '''
    [32500.]
    '''
