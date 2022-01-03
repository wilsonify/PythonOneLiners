from python_one_liners.regular_expressions.regex_one_liner_01 import find_p_then_r


def test_smoke():
    """ smoke """
    print("fire?")


def test_q():
    # Finding Basic Textual Patterns in Strings

    # Dependencies

    # Data
    text = 'peter piper picked a peck of pickled peppers'

    # One-Liner
    result = find_p_then_r(text)

    # Result
    assert result == ['peter', 'piper', 'picked a peck of pickled pepper']
