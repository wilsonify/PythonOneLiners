# Classification with Support-Vector Machines in One Line


# Dependencies
from sklearn import svm
import numpy as np

def mysvc(X):
    return svm.SVC().fit(X[:,:-1], X[:,-1])

if __name__=="__main__":
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
    print(student_0)

    student_1 = svm.predict([[8, 1, 1]])
    print(student_1)

    '''
    ['art']
    ['computer science']
    '''
