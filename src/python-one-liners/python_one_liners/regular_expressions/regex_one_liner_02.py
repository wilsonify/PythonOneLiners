import re

def find_crypto_then_30(text):
    """
    given a string, you will find occurrences in which the string 'crypto' is followed by up to 30 arbitrary characters,
    followed by the string 'coin'.
    """
    matcher = re.compile("crypto(.{1,30})coin")
    groups = matcher.match(text)
    if groups:
        return groups.group(0)
    return groups


if __name__ == "__main__":
    # Writing Your First Web Scraper with Regular Expressions

    # Dependencies


    # Data
    text_1 = "crypto-bot that is trading Bitcoin and other currencies"
    text_2 = "cryptographic encryption methods that can be cracked easily with quantum computers"

    # Result
    print(find_crypto_then_30(text_1))
    print(find_crypto_then_30(text_2))
    '''
    <re.Match object; span=(0, 34), match='crypto-bot that is trading Bitcoin'>
    None
    '''
