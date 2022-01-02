# Decision-Tree Learning in One Line


import numpy as np
from sklearn import tree


def mytree(X):
    return tree.DecisionTreeClassifier(random_state=0).fit(X[:, :-1], X[:, -1])


if __name__ == "__main__":
    ## Data: student scores in (math, language, creativity) --> study field
    X = np.array([[9, 5, 6, "computer science"],
                  [1, 8, 1, "linguistics"],
                  [5, 7, 9, "art"]])

    ## One-liner
    Tree = mytree(X)

    ## Result & puzzle
    student_0 = Tree.predict([[8, 6, 5]])
    print(student_0)

    student_1 = Tree.predict([[3, 7, 9]])
    print(student_1)

    '''
    ['computer science']
    ['linguistics']
    '''
