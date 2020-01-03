import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split



# TODO Implement your own
def split_dataset(x,y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8)
    return x_train, x_test, y_train, y_test

def gradient(w, x, y):
    y_estimate = (x.T * w).flatten()
    error = (y.flatten() - y_estimate)
    gradient = -(1.0/len(x)) * error.dot(x)
    return gradient, np.pow(error, 2)

def read_data(city):
    df = pd.read_csv("../data/amskv_" + city.strip().lower() + ".csv")
    df = df.drop(["Unnamed: 0"], axis=1)
    return df

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

def main():
    data = read_data("beograd")
    x = data["Vreme"]
    y = data["CO [mg.m-3]"]
    x = np.linspace(0,721,721)
    x_train, x_test, y_train, y_test = split_dataset(x, y)
    b = estimate_coef(x_train, y_train)

    plot_regression_line(x, y, b)


if __name__ == "__main__":
    main()

