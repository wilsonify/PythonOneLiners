"""
One-Liner Finding Palindromes with Lambda Functions and Negative Slicing
"""


def is_palindrome(phrase):
    return phrase == phrase[::-1]


if __name__ == "__main__":
    # Result
    print(is_palindrome("anna"))  # True
    print(is_palindrome("kdljfasjf"))  # False
    print(is_palindrome("rats live on no evil star"))  # True
