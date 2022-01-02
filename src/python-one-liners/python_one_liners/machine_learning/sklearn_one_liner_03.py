# K-Means Clustering in One Line


import numpy as np
# Dependencies
from sklearn.cluster import KMeans


class MyKMeans(KMeans):
    def __init__(self):
        super().__init__(n_clusters=2, random_state=0)

    def fit(self, X, y=None, sample_weight=None):
        super().fit(X, y, sample_weight)





if __name__ == "__main__":
    # Data (Work (h) / Salary ($))
    X = np.array([[35, 7000], [45, 6900], [70, 7100],
                  [20, 2000], [25, 2200], [15, 1800]])

    # One-liner
    model = MyKMeans()
    model.fit(X)

    # Result & puzzle
    cc = model.cluster_centers_
    print(cc)
    '''
    [[  20. 2000.]
     [  50. 7000.]]
    '''
