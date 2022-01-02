from python_one_liners.data_science.numpy_one_liner_08 import find_outliers
import numpy as np

def test_smoke():
    print("fire?")


def test_find_outliers():
    # How to Create Advanced Array Filters with Statistics, Math, and Logic

    ## Dependencies
    import numpy as np

    ## Website analytics data:
    ## (row = day), (col = users, bounce, duration)
    a = np.array([[815, 70, 115],
                  [767, 80, 50],
                  [912, 74, 77],
                  [554, 88, 70],
                  [1008, 65, 128]])

    result = find_outliers(a)
    assert result.tolist() == [[1008, 65, 128]]
