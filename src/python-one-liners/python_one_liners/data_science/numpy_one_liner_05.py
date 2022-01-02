# Broadcasting, Slice Assignment, and Reshaping to Clean Every i-th Array Element
import numpy as np


def fill_average(tmp):
    """
    given an array of temperature values,
    replace every seventh temperature value with the average of the last seven days
    (including the seventh day’s temperature value).
    """
    return np.average(tmp.reshape((-1, 7)), axis=1)


if __name__ == "__main__":
    ## Dependencies

    ## Sensor data (Mo, Tu, We, Th, Fr, Sa, Su)
    tmp = np.array([1, 2, 3, 4, 3, 4, 4,
                    5, 3, 3, 4, 3, 4, 6,
                    6, 5, 5, 5, 4, 5, 5])

    ## One-liner
    tmp[6::7] = fill_average(tmp)

    ## Result
    print(tmp)
    '''
    [1 2 3 4 3 4 3 5 3 3 4 3 4 4 6 5 5 5 4 5 5]
    '''
