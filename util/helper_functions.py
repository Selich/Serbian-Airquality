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

