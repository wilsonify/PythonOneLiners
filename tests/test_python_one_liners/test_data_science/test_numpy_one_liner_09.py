from python_one_liners.data_science.numpy_one_liner_09 import find_copurchases


def test_smoke():
    print("fire?")


def test_find_copurchases():
    # Simple Association Analysis: People Who Bought X Also Bought Y

    ## Dependencies
    import numpy as np

    ## Data: row is customer shopping basket
    ## row = [course 1, course 2, ebook 1, ebook 2]
    ## value 1 indicates that an item was bought.
    basket = np.array([[0, 1, 1, 0],
                       [0, 0, 0, 1],
                       [1, 1, 0, 0],
                       [0, 1, 1, 1],
                       [1, 1, 1, 0],
                       [0, 1, 1, 0],
                       [1, 1, 0, 1],
                       [1, 1, 1, 1]])

    ## One-liner
    copurchases = find_copurchases(basket)

    ## Result
    assert copurchases == 0.25
