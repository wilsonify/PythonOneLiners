from python_one_liners.regular_expressions.regex_one_liner_05 import find_valid_urls


def test_smoke():
    """ smoke """
    print("fire?")


def test_q():
    # Finding Nonsecure HTTP URLs

    # Dependencies

    # Data
    article = '''
    The algorithm has important practical applications
    http://blog.finxter.com/applications/
    in many basic data structures such as sets, trees,
    dictionaries, bags, bag trees, bag dictionaries,
    hash sets, https://blog.finxter.com/sets-in-python/
    hash tables, maps, and arrays. http://blog.finxter.com/
    http://not-a-valid-url
    http:/bla.ba.com
    http://bo.bo.bo.bo.bo.bo/
    http://bo.bo.bo.bo.bo.bo/333483--33343-/
    '''

    # One-Liner
    stale_links = find_valid_urls(article)

    # Results
    assert stale_links == [
        'http://blog.finxter.com/applications/', 'http://blog.finxter.com/',
        'http://bo.bo.bo.bo.bo.bo/', 'http://bo.bo.bo.bo.bo.bo/333483--33343-/'
    ]
