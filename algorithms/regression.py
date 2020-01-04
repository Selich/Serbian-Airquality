import numpy as np
import numpy.fft as fft
import numpy.linalg as npl
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split


class LinearRegression:

    def predict(self, X):
        return np.dot(X, self._W)

    def _gradient_descent_step(self, X, targets, lr):
        predictions = self.predict(X)

        error = predictions - targets
        gradient = np.dot(X.T, error) / len(X)

        self._W -= lr * gradient

    def fit(self, X, y, n_iter=100000, lr=0.01):
        self._W = np.zeros(X.shape[1])

        for i in range(n_iter):
            self._gradient_descent_step(x, y, lr)

        return self

def derivative(theta, x, y):
    derivative = []
    dt0 = 0
    dt1 = 0
    for i in range(0, len(x)):
        dt0 = dt0 + (h(theta[0], theta[1], x[i]) - y[i])
        dt1 = dt1 + (h(theta[0], theta[1], x[i]) - y[i]) * x[i]
    dt0 = dt0 / len(x)
    dt1 = dt1 / len(x)
    return [dt0, dt1]

# TODO Implement your own
def split_dataset(x,y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8)
    return x_train, x_test, y_train, y_test

def gradient(w, x, y):
    y_estimate = (x.T * w).flatten()
    error = (y.flatten() - y_estimate)
    gradient = -(1.0/len(x)) * error.dot(x)
    return gradient, np.pow(error, 2)



def rmse(y,y_hat):
    return np.sqrt((np.sum((y_hat - y) ** 2))/ len(y))


def estimate_coef(x, y):
    n = np.size(x)
    m_x, m_y = np.mean(x), np.mean(y)
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)

def plot_regression_line(x, y, b):
    plt.xlabel('x')
    plt.ylabel('y')

    plt.scatter(x, y, color="m", marker="o", s=30)
    y_pred = b[0] + b[1] * x
    plt.plot(x, y_pred, color="g")
    plt.show()

def loss(h, y):
  sq_error = (h - y)**2
  n = len(y)
  return 1.0 / (2*n) * sq_error.sum()

# TODO CO ne moze linearno -> previse je kompleksno kretanje
def main():
    data = read_data("beograd")
    x = data["Vreme"]
    y = data["CO [mg.m-3]"]
    y = y[y < 3.2]
    x = np.linspace(0,len(y),len(y))
    x_train, x_test, y_train, y_test = split_dataset(x, y)
    b = estimate_coef(x_train, y_train)

    y_pred = plot_regression_line(x, y, b)



if __name__ == "__main__":
    main()

