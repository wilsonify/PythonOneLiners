import re

from python_one_liners.regular_expressions.regex_one_liner_08 import find_words_with_duplicate_chars


def test_smoke():
    """ smoke """
    print("fire?")



def test_q():
    # Duplicate Detection in Strings

    # Dependencies
    import re

    # Data
    text = '''
    It was a bright cold day in April, and the clocks were
    striking thirteen. Winston Smith, his chin nuzzled into
    his breast in an effort to escape the vile wind, slipped
    quickly through the glass doors of Victory Mansions,
    though not quickly enough to prevent a swirl of gritty
    dust from entering along with him.
    -- George Orwell, 1984
    '''

    # One-Liner
    duplicates = find_words_with_duplicate_chars(text)

    ## Results
    assert duplicates == [
        ('thirteen.', 'e'), ('nuzzled', 'z'), ('effort', 'f'), ('slipped', 'p'), ('glass', 's'),
        ('doors', 'o'), ('gritty', 't'), ('--', '-'), ('Orwell,', 'l')
    ]
