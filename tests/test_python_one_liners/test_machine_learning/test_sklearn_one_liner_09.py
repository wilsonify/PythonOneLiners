from python_one_liners.machine_learning.sklearn_one_liner_09 import mysvc


def test_smoke():
    print("fire?")


def test_mysvc():
    # Classification with Support-Vector Machines in One Line

    # Dependencies
    import numpy as np

    # Data: student scores in (math, language, creativity) --> study field
    X = np.array([[9, 5, 6, "computer science"],
                  [10, 1, 2, "computer science"],
                  [1, 8, 1, "literature"],
                  [4, 9, 3, "literature"],
                  [0, 1, 10, "art"],
                  [5, 7, 9, "art"]])

    # One-liner
    svm = mysvc(X)

    # Result & puzzle
    student_0 = svm.predict([[3, 3, 6]])
    assert student_0 == 'art'

    student_1 = svm.predict([[8, 1, 1]])
    assert student_1 == 'computer science'
