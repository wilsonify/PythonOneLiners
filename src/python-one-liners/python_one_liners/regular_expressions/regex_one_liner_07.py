"""
Validating the Time Format of User Input, Part 2
"""
import re


def input_ok(text):
    """
    checks whether text has the (time) format XX:XX,
    where X is a number between 0 and 9.
    Additionally, the given time must be a valid time format in the 24-hour time ranging from 00:00 to 23:59.
    :return:
    """
    return re.fullmatch('([01][0-9]|2[0-3]):[0-5][0-9]', text) is not None


if __name__ == "__main__":

    # Dependencies

    # Data
    inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']

    # One-Liner

    # Result
    for x in inputs:
        print(input_ok(x))
    '''
    True
    True
    False
    False
    False
    False
    '''
