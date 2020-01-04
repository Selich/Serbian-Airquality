import numpy as np
import pandas as pd

def loss_fn(X, Y, beta):
    return np.linalg.norm(np.matmul(X, beta) - Y)**2

def regularizer(beta):
    return np.linalg.norm(beta)

def objective_fn(X, Y, beta, lambd):
    return loss_fn(X, Y, beta) + lambd * regularizer(beta)

def mse(X, Y, beta):
    return (1.0 / X.shape[0]) * loss_fn(X, Y, beta).value


def split_dataset(x,y):
    train_size = int(round(len(x) * 0.8))  # Training set size: 75% of full data set.

    x_train = x[:train_size]
    x_test = x[train_size:]
    y_train = x[:train_size]
    y_test = x[train_size:]
    return x_train, x_test, y_train, y_test


def read_data(city):
    df = pd.read_csv("./data/amskv_" + city.strip().lower() + ".csv")
    df = df.drop(["Unnamed: 0"], axis=1)
    return df
