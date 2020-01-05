
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from algorithms.ridge import Ridge
from util.helper_functions import read_data, split_dataset

def main():
    data = read_data("beograd")
    x = data["Vreme"].values
    x = np.linspace(0, len(x), len(x))
    y = data["CO [mg.m-3]"].ffill(axis=0).values
    x_train, x_test, y_train, y_test = split_dataset(x,y)
    model = Ridge(1.)
    model.fit(x, y)
    b, a = model.w_
    plt.scatter(x, y, color="g")
    xmax = x.max()
    plt.plot([0, xmax], [b, b + a * xmax], color="k")
    plt.show()



if __name__ == "__main__":
    main()