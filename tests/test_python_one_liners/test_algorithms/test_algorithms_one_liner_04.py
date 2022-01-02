from python_one_liners.algorithms.algorithms_one_liner_04 import ls, ls_ml


def test_smoke():
    print("fire?")


def test_levenshtein_distance():
    # Finding the Levenshtein Distance
    ## The Data
    a = "cat"
    b = "chello"
    c = "chess"
    assert ls(a, b) == 5
    assert ls(a, c) == 4
    assert ls(b, c) == 3

def test_levenshtein_distance_multiline():
    # Finding the Levenshtein Distance
    ## The Data
    a = "cat"
    b = "chello"
    c = "chess"
    assert ls_ml(a, b) == 5
    assert ls_ml(a, c) == 4
    assert ls_ml(b, c) == 3