# When to Use the sort() Function and When to Use the argsort() Function in NumPy

import numpy as np


def find_names_of_top_three(students, sat_scores):
    """
    find the names of the top three students with the highest SAT scores.
    Note that you’ll ask for the student names and not the sorted SAT scores.
    :return:
    """
    return students[np.argsort(sat_scores)][:-4:-1]


if __name__ == "__main__":
    # Dependencies

    # Data: SAT scores for different students
    sat_scores_outer = np.array([1100, 1256, 1543, 1043, 989, 1412, 1343])
    students_outer = np.array(["John", "Bob", "Alice", "Joe", "Jane", "Frank", "Carl"])

    # One-liner
    top_3 = find_names_of_top_three(students_outer, sat_scores_outer)

    # Result
    print(top_3)
    """
    ['Alice' 'Frank' 'Carl']
    """
