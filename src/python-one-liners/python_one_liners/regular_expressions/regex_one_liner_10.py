# Modifying Regex Patterns in a Multiline String

import re


def substitute(text):
    """ replace Alice Wonderland with Alice Doe """
    return re.sub("Alice Wonderland(?!')", 'Alice Doe', text)


if __name__ == "__main__":
    '''
    expected output:

        Alice Doe married John Doe.
        The new name of former 'Alice Wonderland' is Alice Doe.
        Alice Doe replaces her old name 'Wonderland' with her new name 'Doe'.
        Alice's sister Jane Wonderland still keeps her old name.

    '''
    # Data
    text_outer = '''
    Alice Wonderland married John Doe.
    The new name of former 'Alice Wonderland' is Alice Doe.
    Alice Wonderland replaces her old name 'Wonderland' with her new name 'Doe'.
    Alice's sister Jane Wonderland still keeps her old name.
    '''

    # One-Liner
    updated_text = substitute(text_outer)

    # Result
    print(updated_text)
