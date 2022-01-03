"""
you want to investigate all monetary numbers from a given company report.
"""
import re


def find_dollar_amounts(report):
    """
    given a string, find a list of all occurrences of dollar amounts with optional decimal values.
    The following are valid matches: $10, $10., or $10.00021.
    :param report:
    :return:
    """

    return [x[0] for x in re.findall('(\$[0-9]+(\.[0-9]*)?)', report)]


if __name__ == "__main__":
    # Extracting Dollars from a String

    # Dependencies

    # Data
    report = '''
    If you invested $1 in the year 1801, you would have $18087791.41 today.
    This is a 7.967% return on investment.
    But if you invested only $0.25 in 1801, you would end up with $4521947.8525.
    '''

    # One-Liner
    dollars = find_dollar_amounts(report)

    # Result
    print(dollars)
    '''
    ['$1', '$18087791.41', '$0.25', '$4521947.8525']
    '''
