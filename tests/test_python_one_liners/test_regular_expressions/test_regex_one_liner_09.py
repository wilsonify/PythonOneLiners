from python_one_liners.regular_expressions.regex_one_liner_09 import find_repeat_less_than_10


def test_smoke():
    """ smoke """
    print("fire?")


def test_q():
    # Detecting Word Repetitions

    # Dependencies

    # Data
    text = 'if you use words too often words become used'

    # One-Liner
    style_problems = find_repeat_less_than_10(text)

    # Results
    assert style_problems.group(0) == ' words too often words '
