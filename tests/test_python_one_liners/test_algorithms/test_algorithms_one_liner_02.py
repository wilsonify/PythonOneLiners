from python_one_liners.algorithms.algorithms_one_liner_02 import is_palindrome


def test_smoke():
    print("fire?")


def test_is_palindrome():
    # Finding Palindromes with Lambda Functions and Negative Slicing
    assert is_palindrome("anna")
    assert not is_palindrome("kdljfasjf")
    assert is_palindrome("rats live on no evil star")
