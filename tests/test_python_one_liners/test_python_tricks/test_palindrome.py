def test_smoke():
    print("fire?")


def is_palindrome(phrase):
    return phrase.find(phrase[::-1])


def test_q():
    assert is_palindrome("hello") == -1
    assert is_palindrome("lonelytylenol") == 0
