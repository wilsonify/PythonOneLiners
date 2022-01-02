"""
test for numpy_one_liner_10
"""

from python_one_liners.data_science.numpy_one_liner_10 import find_most_copurchased


def test_smoke():
    """ smoke """
    print("fire?")


def test_find_most_copurchased(basket):
    """ Intermediate Association Analysis to Find Bestseller Bundles """
    # Data: row is customer shopping basket
    # row = [course 1, course 2, ebook 1, ebook 2]
    # value 1 indicates that an item was bought.
    # One-liner
    result = find_most_copurchased(basket)
    assert result == (1, 2, 5)
