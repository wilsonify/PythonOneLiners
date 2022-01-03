"""
# Finding Basic Textual Patterns in Strings
Our input is a string,
and our goal is to use a nongreedy approach to find all patterns that start with the character 'p',
end with the character 'r', and have at least one occurrence of the character 'e'
(and, possibly, an arbitrary number of other characters) in between!

These types of text queries occur quite frequently especially in companies that focus on
text processing, speech recognition, or machine translation
(such as search engines, social networks, or video platforms).
"""
import re


def find_p_then_r(text):
    """ find all patterns that
    start with the character 'p',
    end with the character 'r',
    and have at least one occurrence of the character 'e'
    """
    return re.findall('p.*?e.*?r', text)


if __name__ == "__main__":
    # Dependencies

    # Data
    text_outer = 'peter piper picked a peck of pickled peppers'

    # One-Liner
    result = find_p_then_r(text_outer)

    # Result
    print(result)  # ['peter', 'piper', 'picked a peck of pickled pepper']
