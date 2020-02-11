import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from util.aqi import AQI
from algorithms.metrics.Metric import Metric
from sklearn.model_selection import train_test_split
from algorithms.Regression import *

def test_aqi(data, obelezije):
    x = data["Vreme"].values
    x = np.linspace(0, len(x), len(x))
    y = data[obelezije].ffill(axis=0).values

    concentration = y[568]
    print("Koncentracija CO: " , concentration)

    aqi = AQI(concentration, "CO")
    print("AQI vrednost: ", aqi.get_value())

def test_prediction(data, val):
    metric = Metric(y_test, yy_test)

    R2 = metric.eval("r2")
    mae = metric.eval("mae")
    rmse = metric.eval("rmse")
    print("R2: " + str(R2))
    print("mae: " + str(mae))
    print("mse: " + str(rmse))

    plt.show()
