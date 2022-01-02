import numpy as np

from python_one_liners.data_science.numpy_one_liner_07 import predict_bestseller


def test_smoke():
    print("fire?")


def test_q():
    # How to Use Lambda Functions and Boolean Indexing to Filter Arrays

    ## Dependencies

    ## Data (row = [title, rating])
    books = np.array([['Coffee Break NumPy', 4.6],
                      ['Lord of the Rings', 5.0],
                      ['Harry Potter', 4.3],
                      ['Winnie-the-Pooh', 3.9],
                      ['The Clown of God', 2.2],
                      ['Coffee Break Python', 4.7]])

    ## Results
    assert predict_bestseller(books, 3.9).tolist() == [
        ['Coffee Break NumPy', '4.6'],
        ['Lord of the Rings', '5.0'],
        ['Harry Potter', '4.3'],
        ['Coffee Break Python', '4.7']
    ]
