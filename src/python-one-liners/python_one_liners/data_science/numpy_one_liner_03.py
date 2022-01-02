"""
# Conditional Array Search, Filtering, and Broadcasting to Detect Outliers
"""
import numpy as np


def find_above_average(cities, X):
    """
    finds the cities with above-average observed AQI values
    :param cities:
    :return:
    """
    return set(cities[np.nonzero(X > np.average(X))[0]])


if __name__ == "__main__":
    ## Dependencies

    ## Data: air quality index AQI data (row = city)
    X = np.array(
        [[42, 40, 41, 43, 44, 43],  # Hong Kong
         [30, 31, 29, 29, 29, 30],  # New York
         [8, 13, 31, 11, 11, 9],  # Berlin
         [11, 11, 12, 13, 11, 12]])  # Montreal
    cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])

    ## One-liner
    polluted = find_above_average(cities,X)

    ## Result
    print(polluted)
    '''
    {'Berlin', 'Hong Kong', 'New York'}
    '''
