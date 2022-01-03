import pytest

from python_one_liners.regular_expressions.regex_one_liner_06 import input_ok


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
            ('99:99', True)
    )
)
def test_q(x, expected):
    assert input_ok(x) == expected
