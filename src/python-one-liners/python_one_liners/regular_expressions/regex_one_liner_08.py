# Duplicate Detection in Strings
import re


def find_words_with_duplicate_chars(text):
    """
    find all words that contain duplicate characters.
    A word in this case is defined as any series of non-whitespace characters
    separated by an arbitrary number of whitespace characters.
    :return:
    """
    return re.findall('([^\s]*(?P<x>[^\s])(?P=x)[^\s]*)', text)


if __name__ == "__main__":
    # Dependencies

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

    # Results
    print(duplicates)
    '''
    [('thirteen.', 'e'), ('nuzzled', 'z'), ('effort', 'f'),
    ('slipped', 'p'), ('glass', 's'), ('doors', 'o'),
    ('gritty', 't'), ('--', '-'), ('Orwell,', 'l')]
    '''
