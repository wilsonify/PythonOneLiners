import re

def find_puzzle_links(page):
    """
    given a string,
    find all hyperlinks that point to the domain finxter.com
    and contain the strings 'test' or 'puzzle' in the link description.
    """
    return re.findall("(<a.*?finxter.*?(test|puzzle).*?>)", page)


if __name__ == "__main__":
    # Analyzing Hyperlinks of HTML Documents

    # Dependencies


    # Data
    page = '''
    <!DOCTYPE html>
    <html>
    <body>
    <h1>My Programming Links</h1>
    <a href="https://app.finxter.com/">test your Python skills</a>
    <a href="https://blog.finxter.com/recursion/">Learn recursion</a>
    <a href="https://nostarch.com/">Great books from NoStarchPress</a>
    <a href="http://finxter.com/">Solve more Python puzzles</a>
    </body>
    </html>
    '''

    # One-Liner
    practice_tests = find_puzzle_links(page)

    # Result
    print(practice_tests)
    '''
    [('<a href="https://app.finxter.com/">test your Python skills</a>', 'test'),
     ('<a href="http://finxter.com/">Solve more Python puzzles</a>', 'puzzle')]
    '''
