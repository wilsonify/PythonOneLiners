from python_one_liners.regular_expressions.regex_one_liner_10 import substitute

def test_smoke():
    """ smoke """
    print("fire?")

def test_q():
    text = '''
Alice Wonderland married John Doe.
The new name of former 'Alice Wonderland' is Alice Doe.
Alice Wonderland replaces her old name 'Wonderland' with her new name 'Doe'.
Alice's sister Jane Wonderland still keeps her old name.
'''

    updated_text = substitute(text)

    assert updated_text == (
        '\n'
        'Alice Doe married John Doe.\n'
        "The new name of former 'Alice Wonderland' is Alice Doe.\n"
        "Alice Doe replaces her old name 'Wonderland' with her new name 'Doe'.\n"
        "Alice's sister Jane Wonderland still keeps her old name.\n"
        ''
    )
