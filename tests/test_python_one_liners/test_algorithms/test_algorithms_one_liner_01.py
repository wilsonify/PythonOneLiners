from python_one_liners.algorithms.algorithms_one_liner_01 import is_anagram


def test_smoke():
    print("fire?")


def test_anagrams():
    # Finding Anagrams with Lambda Functions and Sorting
    assert is_anagram("elvis", "lives")
    assert is_anagram("elvise", "livees")
    assert not is_anagram("elvis", "dead")
