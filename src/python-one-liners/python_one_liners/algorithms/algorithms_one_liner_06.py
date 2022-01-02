"""
One-Liner Caesar’s Cipher Encryption Using Advanced Indexing and List Comprehension
"""


def rt13(x):
    return "".join([abc[(abc.find(c) + 13) % 26] for c in x])


if __name__ == "__main__":
    # Data
    abc = "abcdefghijklmnopqrstuvwxyz"
    s = "xthexrussiansxarexcoming"
    # Result
    print(rt13(s))  # kgurkehffvnafknerkpbzvat
    print(rt13(rt13(s)))  # xthexrussiansxarexcoming
