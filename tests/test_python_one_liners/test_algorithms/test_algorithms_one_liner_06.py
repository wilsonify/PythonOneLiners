from python_one_liners.algorithms.algorithms_one_liner_06 import rt13


def test_smoke():
    print("fire?")


def test_rt13():
    # Caesar’s Cipher Encryption Using Advanced Indexing and List Comprehension
    abc = "abcdefghijklmnopqrstuvwxyz"
    s = "xthexrussiansxarexcoming"
    assert rt13(s) == "kgurkehffvnafknerkpbzvat"
    assert rt13(rt13(s)) == "xthexrussiansxarexcoming"
