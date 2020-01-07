import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from util.aqi import AQI
from sklearn.model_selection import train_test_split
from algorithms.Regression import *


def test_ridge(data):
    x = data["Vreme"].values
    x = np.linspace(0, len(x), len(x))
    y = data["CO [mg.m-3]"].ffill(axis=0).values
    model = Regression(1.)
    model.fit(x, y, "ridge")
    b, a = model.w
    plt.scatter(x, y, color="g")
    plt.plot([0, x.max], [b, b + a * x.max], color="k")
    plt.show()


def test_aqi(data):
    x = data["Vreme"].values
    x = np.linspace(0, len(x), len(x))
    y = data["CO [mg.m-3]"].ffill(axis=0).values

    concentration = y[568]
    print(concentration)

    aqi = AQI(concentration, "CO")
    print(aqi.get_value())


def test_metrics(x, y, model: Model):
    yy = model.predict
    r2_ret = R2(y, yy)
    return r2_ret



def test_prediction(data):
    x = data["Vreme"].values
    x = np.linspace(0, len(x), len(x))
    y = data["CO [mg.m-3]"].ffill(axis=0).values
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    model = Regression(1.)
    model.fit(x_train, y_train, "ridge")
    b, a = model.w
    plt.scatter(x, y, color="g")
    plt.plot([0, x_train.max()], [b, b + a * x_train.max()], color="k")
    plt.plot([x_train[0], x_test.max()], [b, b + a * x_test.max()], color="r")
    plt.show()
