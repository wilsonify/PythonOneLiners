import numpy as np
from python_one_liners.machine_learning.sklearn_one_liner_06 import mytree


def test_smoke():
    print("fire?")


def test_mytree():
    # Decision-Tree Learning in One Line

    # Dependencies


    # Data: student scores in (math, language, creativity) --> study field
    X = np.array([[9, 5, 6, "computer science"],
                  [1, 8, 1, "linguistics"],
                  [5, 7, 9, "art"]])

    # One-liner
    Tree = mytree(X)

    # Result & puzzle
    student_0 = Tree.predict([[8, 6, 5]])
    assert student_0 == 'computer science'

    student_1 = Tree.predict([[3, 7, 9]])
    assert student_1 == 'art'
