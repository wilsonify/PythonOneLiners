import re


def input_ok(text):
    """
    checks whether text has the (time) format XX:XX,
    where X is a number between 0 and 9.

    :return:
    """
    return re.fullmatch('[0-9]{2}:[0-9]{2}', text) is not None


if __name__ == "__main__":
    # Validating the Time Format of User Input, Part 1

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
    True
    '''
