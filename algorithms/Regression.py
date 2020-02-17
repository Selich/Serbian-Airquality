import numpy as np
from collections import OrderedDict
import pandas as pd
from scipy import linalg
from util.data_processing import *
from util.testing_functions import *
from algorithms.AQI import AQI

gradovi = [ "novisad", "beograd", "uzice", "cacak", "nis" ]
        
def mse(y,yy,theta):
    tobesummed = np.power((y-yy),2)
    return np.sum(tobesummed)/(2 * len(y))

def norm(data):
    data = (data - data.min()) / (data.max() - data.min())
    return data

def gradient_descent(X,y,theta,iters,alpha):
    cost = np.zeros(iters)
    for i in range(iters):
        theta = theta - (alpha/len(X)) * np.sum(X * (X @ theta.T - y), axis=0)
        cost[i] = mse(X, y, theta)
    
    return theta,cost

def aqi_calc():
    # hiperparametri
    alpha = 0.01
    iters = 1000

    novisad = read_data("novisad")
    atributi = [
        "NO2 [ug.m-3]","SO2 [ug.m-3]","CO [mg.m-3]"
    ]

    data = novisad[atributi].ffill(axis=0)

    # data = norm(data)
    data.drop(data.tail(1).index,inplace=True)
    for i in data.index:
        val1 = AQI(data.loc[i,atributi[0]],atributi[0]).get_value()
        val2 = AQI(data.loc[i,atributi[1]],atributi[1]).get_value()
        val3 = AQI(data.loc[i,atributi[2]],atributi[2]).get_value()
        data.loc[i,"AQI"] = max( val1, val2, val3 )

    model = MultiVariant(3,alpha,iters)
    model.fit(data)
    return model.w

def find_and_save_aqi(city, atributi):
    w = aqi_calc()

    data = read_data(city)
    data = data[atributi]

    X1 = norm(data.iloc[:,0:2])
    ones = np.ones([X1.shape[0],1])
    X1 = np.concatenate((ones,X1),axis=1)

    yy = (X1 @ w.T)
    np.savetxt("./data/aqi_" + city + ".csv", yy, delimiter=",")
    return yy

def test_prediction(y_test, yy_test):
    metric = Metric(y_test, yy_test)

    R2 = metric.eval("r2")
    mae = metric.eval("mae")
    rmse = metric.eval("rmse")
    print("R2: " + str(R2))
    print("mae: " + str(mae))
    print("mse: " + str(rmse))
    
def predict(city, interval, stepen):
    data = read_data(city)
    data.drop(data.tail(1).index,inplace=True)
    x = data["Vreme"].values
    y = pd.read_csv("./data/aqi_" + city + ".csv")
    x = np.linspace(0,len(x),len(x))

    x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.8, test_size=0.2)

    model = Regression()
    return model.fit(x_train,y_train,stepen)

class MultiVariant():

    def __init__(self,num_dots = 3,alpha=0.01,iters=1000):
        self.w = None
        self.theta = np.zeros([1,num_dots])
        self.alpha = alpha
        self.iters = iters

    def fit(self, data):
        theta = self.theta
        alpha = self.alpha
        iters = self.iters
        X1 = data.iloc[:,0:2]
        X1 = norm(X1)

        ones = np.ones([X1.shape[0],1])
        X1 = np.concatenate((ones,X1),axis=1)

        y = data.iloc[:,3:4].values 

        x1_train, x1_test, y_train, y_test = train_test_split(X1,y)

        w,cost = gradient_descent(x1_train,y_train,theta,iters,alpha) 
        yy = (x1_test @ w.T)
        yy2 = (X1 @ w.T)
        self.w = w

class Regression():

    def __init__(self):
            self.w = None
            self.lambda_ = 0.1


    def fit(self, x, t, stepen, mode="ridge"):
        if stepen == 1:
            Xtil = np.c_[np.ones(x.shape[0]), x]
            c = np.eye(Xtil.shape[1])
        
            if mode.lower() == "ridge":
                c = c ** 2
            elif mode.lower() == "lasso":
                c = np.linalg.norm(c)

            a = np.dot(Xtil.T, Xtil) + self.lambda_ * c
            b = np.dot(Xtil.T, t)
            self.w = linalg.solve(a, b)
            # return self.w[0] + self.w[1] * x
        elif stepen == 2:
            self.w = np.polyfit(x,t,2)
            # return self.w[2] + self.w[1] * x + self.w[0] * x ** 2
        elif stepen == 3:
            self.w = np.polyfit(x,t,3)
            # return self.w[3] + self.w[2] * x + self.w[1] * x ** 2 + self.w[0] * x ** 3
        return self.w

        