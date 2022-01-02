# How to Use Lambda Functions and Boolean Indexing to Filter Arrays
import numpy as np


def predict_bestseller(x, y):
    """
    create a filter function that takes a list of books x and a minimum rating y
    and returns a list of potential bestsellers that have higher than minimum rating
    :return:
    """
    return x[x[:, 1].astype(float) > y]


if __name__ == "__main__":
    ## Dependencies

    ## Data (row = [title, rating])
    books = np.array([['Coffee Break NumPy', 4.6],
                      ['Lord of the Rings', 5.0],
                      ['Harry Potter', 4.3],
                      ['Winnie-the-Pooh', 3.9],
                      ['The Clown of God', 2.2],
                      ['Coffee Break Python', 4.7]])

    ## Results
    print(predict_bestseller(books, 3.9))
    '''
    [['Coffee Break NumPy' '4.6']
     ['Lord of the Rings' '5.0']
     ['Harry Potter' '4.3']
     ['Coffee Break Python' '4.7']]
    '''
