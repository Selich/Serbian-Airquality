import numpy as np
from scipy import linalg


class Ridge:

    def __init__(self, lambda_=1.):
        self.lambda_ = lambda_  # λ
        self.w_ = None

    def fit(self, X, t):
        Xtil = np.c_[np.ones(X.shape[0]), X]
        c = np.eye(Xtil.shape[1])
        A = np.dot(Xtil.T, Xtil) + self.lambda_ * c
        b = np.dot(Xtil.T, t)
        self.w_ = linalg.solve(A, b)

    def predict(self, X):
        Xtil = np.c_[np.ones()]
        return np.dot(Xtil, self.w_)