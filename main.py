
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from algorithms.ridge import Ridge
from util.helper_functions import read_data, split_dataset
from sklearn.model_selection import train_test_split
from util.aqi import AQI

def test_ridge():
    data = read_data("beograd")
    x = data["Vreme"].values
    x = np.linspace(0, len(x), len(x))
    y = data["CO [mg.m-3]"].ffill(axis=0).values
    model.fit(x, y)
    b, a = model.w
    plt.scatter(x, y, color="g")
    plt.plot([0, x.max()], [b, b + a * x.max()], color="k")
    plt.show()

def test_aqi():
    data = read_data("beograd")
    x = data["Vreme"].values
    x = np.linspace(0, len(x), len(x))
    y = data["CO [mg.m-3]"].ffill(axis=0).values

    conc = y[568]
    print(conc)

    aqi = AQI(conc,"CO")
    print(aqi.get_value())


def test_prediction():
    data = read_data("beograd")
    x = data["Vreme"].values
    x = np.linspace(0, len(x), len(x))
    y = data["CO [mg.m-3]"].ffill(axis=0).values
    x_train, x_test, y_train, y_test = train_test_split(x,y)
    model = Ridge(1.)
    model.fit(x_train, y_train)
    b, a = model.w
    plt.scatter(x, y, color="g")
    plt.plot([0, x_train.max()], [b, b + a * x_train.max()], color="k")
    plt.plot([x_train[0], x_test.max()], [b, b + a * x_test.max()], color="r")
    plt.show()


def main():
    test_prediction()



if __name__ == "__main__":
    main()
