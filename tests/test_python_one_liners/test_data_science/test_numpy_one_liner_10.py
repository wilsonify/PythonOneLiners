from python_one_liners.data_science.numpy_one_liner_10 import find_most_copurchased


def test_smoke():
    print("fire?")


def test_find_most_copurchased():
    # Intermediate Association Analysis to Find Bestseller Bundles

    ## Dependencies
    import numpy as np

    ## Data: row is customer shopping basket
    ## row = [course 1, course 2, ebook 1, ebook 2]
    ## value 1 indicates that an item was bought.
    basket = np.array(
        [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1], [1, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1], [1, 1, 1, 1]]
    )

    ## One-liner
    result = find_most_copurchased(basket)
    assert result == (1, 2, 5)
