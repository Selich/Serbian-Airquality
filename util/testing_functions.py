import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from util.aqi import AQI
from algorithms.metrics.Metric import Metric
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


def test_aqi(data, obelezije):
    x = data["Vreme"].values
    x = np.linspace(0, len(x), len(x))
    y = data[obelezije].ffill(axis=0).values

    concentration = y[568]
    print("Koncentracija CO: " , concentration)

    aqi = AQI(concentration, "CO")
    print("AQI vrednost: ", aqi.get_value())


def test_metrics(y, model,tip):
    yy = model.predict(y)
    metric = Metric(y, yy)
    ret = metric.eval(tip)
    return ret


def test_prediction(data, val):
    x = data["Vreme"].values
    x = np.linspace(0, len(x), len(x))
    try:
      y = data[val].ffill(axis=0).values
    except:
      print("Obelezije nije pronadjeno")
      return
    
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    model = Regression(1.)
    model.fit(x_train, y_train, "ridge")
    b, a = model.w
    plt.scatter(x, y, color="g")
    plt.plot([0, len(x_train)], [b, b + a * x_train.max()], color="k")
    plt.plot([len(x_train), x_test.max()], [b, b + a * x_test.max()], color="r")

    yy_test = b + a * x_test

    metric = Metric(y_test, yy_test)

    R2 = metric.eval("r2")
    mae = metric.eval("mae")
    rmse = metric.eval("rmse")
    print("R2: " + str(R2))
    print("mae: " + str(mae))
    print("mse: " + str(rmse))

    plt.show()
