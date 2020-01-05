import numpy as np
from scipy import linalg

class LinearRegression:

    def __init__(self):
        self.w_ = None

    def fit(self, X, t):

        Xtil = np.c_[np.ones(X.shape[0]), X]
        A = np.dot(Xtil.T, Xtil)

        self.w_ = linalg.solve(A, b)

    def predict(self, X):

        if X.ndim == 1:
            X = X.reshape(1, -1)
        Xtil = np.c_[np.ones(X.shape[0]), X]
        return np.dot(Xtil, self.w_)


if __name__ == "__main__":
    pass