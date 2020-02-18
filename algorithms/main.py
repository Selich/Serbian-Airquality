from polynomial_regression import PolynomialRegression
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np 

def main():
    # numpy oba
    city = "nis"
    y = pd.read_csv("../data/aqi_" + city + ".csv")
    y = y.to_numpy()
    y = y[-100:]
    x = np.linspace(0, len(y), len(y))

    x_train, x_test, y_train, y_test = train_test_split(x,y)

    PR = PolynomialRegression(x, y)
    theta = PR.fit(order = 2, tol = 10**-3, numIters = 100, alpha = 10**-3)
    PR.plot_predicted()
    PR.plot_cost()

if __name__ == "__main__":
    main()
