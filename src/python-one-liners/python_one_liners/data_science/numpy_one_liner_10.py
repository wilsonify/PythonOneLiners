# Intermediate Association Analysis to Find Bestseller Bundles
import numpy as np

def find_most_copurchased(basket):
    """
    find the two items that were purchased most often together
    """
    copurchases = [(i, j, np.sum(basket[:, i] + basket[:, j] == 2)) for i in range(4) for j in range(i + 1, 4)]
    return max(copurchases, key=lambda x: x[2])

if __name__=="__main__":
    ## Dependencies


    ## Data: row is customer shopping basket
    ## row = [course 1, course 2, ebook 1, ebook 2]
    ## value 1 indicates that an item was bought.
    basket = np.array(
        [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1], [1, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1], [1, 1, 1, 1]]
    )

    ## One-liner
    result = find_most_copurchased(basket)

    ## Result
    print(result)
    '''
    (1, 2, 5)
    '''
