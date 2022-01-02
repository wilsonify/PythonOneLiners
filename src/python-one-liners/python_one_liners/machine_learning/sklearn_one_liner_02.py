# Logistic Regression in One Line
import numpy as np
from sklearn.linear_model import LogisticRegression


def mylogreg(X):
    return LogisticRegression().fit(X[:, 0].reshape(-1, 1), X[:, 1])


if __name__ == "__main__":
    ## Data (#cigarettes, cancer)
    X = np.array([[0, "No"],
                  [10, "No"],
                  [60, "Yes"],
                  [90, "Yes"]])

    ## One-liner
    model = mylogreg(X)

    ## Result & puzzle
    print(model.predict([[2], [12], [36], [40], [90]]))
    '''
    ['No' 'No' 'Yes' 'Yes' 'Yes']
    '''
