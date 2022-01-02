from python_one_liners.machine_learning.sklearn_one_liner_02 import mylogreg


def test_smoke():
    print("fire?")


def test_mylogreg():
    # Logistic Regression in One Line
    import numpy as np

    # Data (#cigarettes, cancer)
    X = np.array([[0, "No"],
                  [10, "No"],
                  [60, "Yes"],
                  [90, "Yes"]])

    # One-liner
    model = mylogreg(X)

    # Result & puzzle
    result = model.predict([[2], [12], [37], [40], [90]])
    assert result.tolist() == ['No', 'No', 'Yes', 'Yes', 'Yes']
