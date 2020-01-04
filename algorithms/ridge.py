import numpy as np

class Ridge():

    # beta <-> lambda
    def __init__(self, iters=2000, alpha=0.1, beta=0.1):
        self.iters = iters
        self.alpha = alpha
        self.beta = beta

    def compute_cost(self, X, y, w, beta):
        m = X.shape[0]
        J = (1. / (2. * m)) * \
            (np.sum((np.dot(X, w) - y) ** 2.) + beta * np.dot(w.T, w))

        return J

    def gradient_descent(self, X, y, w, iters, alpha, beta):
        
        m = X.shape[0]
        J_all = np.zeros((iters, 1))

        for i in range(iters):

            J_all[i] = self.compute_cost(X, y, w, beta)

            w = w - (alpha / m) * (np.dot(X.T, (X.dot(w) - y[:, np.newaxis])) + beta * w)

        return w, J_all

    def fit(self, X, y):
        Xn = np.ndarray.copy(X)
        yn = np.ndarray.copy(y)

        w = np.zeros((Xn.shape[1] + 1, 1))

        self.X_mean = np.mean(Xn, axis=0)
        self.X_std = np.std(Xn, axis=0)
        Xn -= self.X_mean
        self.X_std[self.X_std == 0] = 1
        Xn /= self.X_std

        self.y_mean = yn.mean(axis=0)
        yn -= self.y_mean

        Xn = np.hstack((np.ones(Xn.shape[0])[np.newaxis].T, Xn))

        self.w, self.J_all = self.gradient_descent(
            Xn, yn, w, self.iters, self.alpha, self.beta)

    def predict(self, X):
        Xn = np.ndarray.copy(X)

        Xn -= self.X_mean
        Xn /= self.X_std
        Xn = np.hstack((np.ones(Xn.shape[0])[np.newaxis].T, Xn))

        return Xn.dot(self.w) + self.y_mean