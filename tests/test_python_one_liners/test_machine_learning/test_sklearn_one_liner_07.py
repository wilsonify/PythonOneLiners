from python_one_liners.machine_learning.sklearn_one_liner_07 import find_smalled_var


def test_smoke():
    print("fire?")


def test_q():
    # Get Row with Minimal Variance in One Line

    ## Dependencies
    import numpy as np

    ## Data (rows: stocks / cols: stock prices)
    X = np.array([[25, 27, 29, 30],
                  [1, 5, 3, 2],
                  [12, 11, 8, 3],
                  [1, 1, 2, 2],
                  [2, 6, 2, 2]])

    ## One-liner: Find the stock with smallest variance
    min_row = find_smalled_var(X)

    ## Result & puzzle
    # "Row with minimum variance: "
    assert min_row[0] == 3
    # "Variance: "
    assert min_row[1] == 0.25
