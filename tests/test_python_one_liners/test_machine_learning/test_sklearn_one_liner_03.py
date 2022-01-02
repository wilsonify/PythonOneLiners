from python_one_liners.machine_learning.sklearn_one_liner_03 import mykmeans


def test_smoke():
    print("fire?")


def test_mykmeans():
    # K-Means Clustering in One Line

    # Dependencies
    import numpy as np

    # Data (Work (h) / Salary ($))
    X = np.array([[35, 7000], [45, 6900], [70, 7100],
                  [20, 2000], [25, 2200], [15, 1800]])

    # One-liner
    model = mykmeans(X)

    # Result & puzzle
    cc = model.cluster_centers_
    assert cc.tolist() == [[20.0, 2000.0], [50.0, 7000.0]]
