from python_one_liners.machine_learning.sklearn_one_liner_04 import myknn


def test_smoke():
    print("fire?")


def test_q():
    # K-Nearest Neighbors in One Line

    ## Dependencies
    import numpy as np

    ## Data (House Size (square meters) / House Price ($))
    X = np.array([[35, 30000], [45, 45000], [40, 50000],
                  [35, 35000], [25, 32500], [40, 40000]])

    ## One-liner
    KNN = myknn(X)

    ## Result & puzzle
    res = KNN.predict([[30]])
    assert res.tolist() == [32500.]
