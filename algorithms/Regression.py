import numpy as np
import pandas as pd
from algorithms import Model
from scipy import linalg
from util.data_processing import *
from util.testing_functions import *
from util.helper_functions import *
from util.aqi import AQI

gradovi = [ "novisad", "beograd", "uzice", "cacak", "nis" ]
degrees = [i for i in range(1,7)]
def populate_aqi(data: pd.DataFrame):
    aqi_series = pd.Series(index=data.index)
    names = list(data.columns)
    max_aqi = 0
    for idx, row in data.iterrows():
        for name in names:
            try:
                temp_aqi = AQI(row[name], name)
                if temp_aqi > max_aqi:
                    max_aqi = temp_aqi
            except expression as identifier:
                pass
        aqi_series.loc[idx] = max_aqi
    
    return aqi_series
        
        
def mse(y,yy,theta):
    tobesummed = np.power((y-yy),2)
    return np.sum(tobesummed)/(2 * len(y))

def gradient_descent(X,y,theta,iters,alpha):
    cost = np.zeros(iters)
    for i in range(iters):
        theta = theta - (alpha/len(X)) * np.sum(X * (X @ theta.T - y), axis=0)
        cost[i] = mse(X, y, theta)
    
    return theta,cost

def norm(data):
    data = (data - data.min()) / (data.max() - data.min())
    return data

def mutlivar(data, atributi):
    theta = np.zeros([1,3])
    alpha = 0.01
    iters = 1000
    # X1 = data[atributi]
    X1 = data.iloc[:,0:2]
    X2 = data.iloc[:,1:3]
    ones = np.ones([X.shape[0],1])
    X1 = np.concatenate((ones,X),axis=1)
    X2 = np.concatenate((ones,X),axis=1)
    y1 = data.iloc[:,3:4].values 
    y2 = data.iloc[:,3:4].values 

    w,cost = gradient_descent(X,y,theta,iters,alpha) 
    w,cost = gradient_descent(X,y,theta,iters,alpha) 
    return w

def aqi_calc():
    # hiperparametri
    theta = np.zeros([1,3])
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

    X1 = data.iloc[:,0:2]
    X1 = norm(X1)
    ones = np.ones([X1.shape[0],1])
    X1 = np.concatenate((ones,X1),axis=1)
    y = data.iloc[:,3:4].values 

    x1_train, x1_test, y_train, y_test = train_test_split(X1,y)
    w,cost = gradient_descent(x1_train,y_train,theta,iters,alpha) 
    yy = (x1_test @ w.T)
    yy2 = (X1 @ w.T)
    print(w)
    return w

# TODO: Weights in dict for every atribute

def find_aqi(city, atributi):
    w = aqi_calc()

    data = read_data(city)
    data = data[atributi]
    X1 = norm(data.iloc[:,0:2])
    ones = np.ones([X1.shape[0],1])
    X1 = np.concatenate((ones,X1),axis=1)

    yy = (X1 @ w.T)
    yy = np.around(yy, decimals=0)
    np.savetxt("./data/aqi_" + city + ".csv", yy, delimiter=",")
    return yy

def update_weights(x,y):
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    model = Regression(1.)
    model.fit(x_train, y_train,"ridge")
    return model

def test_prediction():
    metric = Metric(y_test, yy_test)

    R2 = metric.eval("r2")
    mae = metric.eval("mae")
    rmse = metric.eval("rmse")
    print("R2: " + str(R2))
    print("mae: " + str(mae))
    print("mse: " + str(rmse))
    
def predict(city, interval):
    data = read_data(city)
    data.drop(data.tail(1).index,inplace=True)
    x = data["Vreme"].values
    y = pd.read_csv("./data/aqi_" + city + ".csv")

    x = np.linspace(0,len(x),len(x))
    model = update_weights(x,y)
    b, a = model.w


    x = np.linspace(0,interval,interval)
    yy = b + a * x
    yy = yy.mean()
    return yy

    


class Regression():

    def __init__(self,lambda_=1., alpha=0.01,iters = 1000):
        self.lambda_ = lambda_
        self.w = None

        

    def fit(self, x, t,mode="ridge") -> None:

        xtil = np.c_[np.ones(x.shape[0]), x]
        c = np.eye(xtil.shape[1])

        if mode.lower() == "ridge":
            c = c ** 2
        elif mode.lower() == "lasso":
            c = np.norm(c)

        a = np.dot(xtil.T, xtil) + self.lambda_ * c
        b = np.dot(xtil.T, t)
        self.w = linalg.solve(a, b)


    def predict(self, x):
        '''
        Primenjujemo odgovarajuce tezine na linearni polinom
        '''
        b, a = self.w
        return b + a * x
