# Simple Association Analysis: People Who Bought X Also Bought Y
import numpy as np


def find_copurchases(basket):
    """
    find fraction of customers who bought two ebooks together?
    the recommender system can offer customers a book “bundle” to buy
    if it sees that they originally intended to buy a single book
    :return:
    """
    return np.sum(np.all(basket[:, 2:], axis=1)) / basket.shape[0]


if __name__ == "__main__":
    ## Dependencies

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
    print(copurchases)
    '''
    0.25
    '''
