""" Detecting Word Repetitions """
import re


def find_repeat_less_than_10(text):
    """
    given a string consisting of lowercase, whitespace-separated words, without special characters.
    Find a matching substring where the first and the last word are the same (repetition)
    and in-between are at most 10 words.
    :return:
    """
    return re.search(r'\s(?P<x>[a-z]+)\s+([a-z]+\s+){0,10}(?P=x)\s', ' ' + text + ' ')


if __name__ == "__main__":
    # Data
    text_outer = 'if you use words too often words become used'

    # One-Liner
    style_problems = find_repeat_less_than_10(text_outer)

    # Results
    print(style_problems)
    '''
    <re.Match object; span=(11, 34), match=' words too often words '>
    '''
