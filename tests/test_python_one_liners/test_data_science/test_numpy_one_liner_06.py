"""
test for numpy_one_liner_06
"""
import numpy as np
from python_one_liners.data_science.numpy_one_liner_06 import find_names_of_top_three


def test_smoke():
    """ smoke """
    print("fire?")


def test_find_names_of_top_three():
    """When to Use the sort() Function and When to Use the argsort() Function in NumPy"""
    # Data: SAT scores for different students
    sat_scores = np.array([1100, 1256, 1543, 1043, 989, 1412, 1343])
    students = np.array(["John", "Bob", "Alice", "Joe", "Jane", "Frank", "Carl"])

    # One-liner
    top_3 = find_names_of_top_three(students, sat_scores)

    # Result
    assert top_3.tolist() == ["Alice", "Frank", "Carl"]
