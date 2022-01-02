import numpy as np

from python_one_liners.data_science.numpy_one_liner_03 import find_above_average


def test_smoke():
    print("fire?")


def test_q():
    # Conditional Array Search, Filtering, and Broadcasting to Detect Outliers

    ## Data: air quality index AQI data (row = city)
    X = np.array(
        [[42, 40, 41, 43, 44, 43],  # Hong Kong
         [30, 31, 29, 29, 29, 30],  # New York
         [8, 13, 31, 11, 11, 9],  # Berlin
         [11, 11, 12, 13, 11, 12]])  # Montreal
    cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])

    ## One-liner
    polluted = find_above_average(cities, X)

    ## Result
    assert polluted == {'Berlin', 'Hong Kong', 'New York'}
