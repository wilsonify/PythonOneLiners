import pytest

from python_one_liners.regular_expressions.regex_one_liner_07 import input_ok


def test_smoke():
    """ smoke """
    print("fire?")


@pytest.mark.parametrize(
    ("x", "expected"), (
            ('18:29', True),
            ('23:55', True),
            ('123', False),
            ('ab:de', False),
            ('18:299', False),
            ('99:99', False)
    )
)
def test_q(x, expected):
    # Validating the Time Format of User Input, Part 2

    # Dependencies

    # Data
    inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']

    # One-Liner

    ## Result
    assert input_ok(x) == expected
    '''
    True
    True
    False
    False
    False
    False
    '''
