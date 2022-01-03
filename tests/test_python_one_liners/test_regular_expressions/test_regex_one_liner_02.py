def test_smoke():
    """ smoke """
    print("fire?")


def test_q():
    # Writing Your First Web Scraper with Regular Expressions

    # Dependencies
    import re

    # Data
    text_1 = "crypto-bot that is trading Bitcoin and other currencies"
    text_2 = "cryptographic encryption methods that can be cracked easily with quantum computers"

    # One-Liner
    pattern = re.compile("crypto(.{1,30})coin")

    assert pattern.match(text_1).group(0) == 'crypto-bot that is trading Bitcoin'
    assert pattern.match(text_2) is None
