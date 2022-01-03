from python_one_liners.regular_expressions.regex_one_liner_04 import find_dollar_amounts


def test_smoke():
    """ smoke """
    print("fire?")


def test_q():
    # Extracting Dollars from a String

    # Dependencies
    import re

    # Data
    report = '''
    If you invested $1 in the year 1801, you would have $18087791.41 today.
    This is a 7.967% return on investment.
    But if you invested only $0.25 in 1801, you would end up with $4521947.8525.
    '''

    # One-Liner
    dollars = find_dollar_amounts(report)

    # Result
    assert dollars == ['$1', '$18087791.41', '$0.25', '$4521947.8525']
