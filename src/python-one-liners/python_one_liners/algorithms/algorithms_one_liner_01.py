def is_anagram(x1, x2):
    # Finding Anagrams with Lambda Functions and Sorting
    return sorted(x1) == sorted(x2)


if __name__ == "__main__":
    ## Results
    print(is_anagram("elvis", "lives"))
    print(is_anagram("elvise", "livees"))
    print(is_anagram("elvis", "dead"))
    '''
    True
    True
    False
    '''
