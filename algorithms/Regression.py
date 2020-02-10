import numpy as np
import pandas as pd
from algorithms import Model
from scipy import linalg


class Regression():

    def __init__(self, x, y, lambda_=1., alpha=0.01,iters = 1000):
        self.x = x
        self.y = y
        self.lambda_ = lambda_
        self.w = None
        self.alpha = alpha
        self.iters = iters
        self.theta = None
        ones = np.ones([x.shape[0],1])
        x = np.concatenate((ones,X),axis=1)

        y = my_data.iloc[:,2:3].values
        self.theta = np.zeros([1,3])

        

    def fit(self, x, t, mode="ridge") -> None:

        '''
        Konkatenaciju matrice oblika
           [ 1 x0
             1 x1
             1 x2

        i konstruisemo vektor c koji ce nam sluziti kao bias


        U zavisnosti kakav bias smo izabrali, koristicemo c

        vektor a i b predstavljaju samu implementaciju date formule

        linalg.solve resava sistem jednacina da bismo dobili odgovarajuce tezine aproksimiranog polinoma

        '''

        xtil = np.c_[np.ones(x.shape[0]), x]
        c = np.eye(xtil.shape[1])

        if mode.lower() == "ridge":
            c = c ** 2
        elif mode.lower() == "lasso":
            c = np.norm(c)

        a = np.dot(xtil.T, xtil) + self.lambda_ * c
        b = np.dot(xtil.T, t)
        self.w = linalg.solve(a, b)



    def calc_cost(self,x,y):

        summ = np.power((( x @ self.theta.T) - y), 2)

        return np.sum(summ)/ ( 2 * len(x))

    def gradient_descend():
        x = self.x
        y = self.y
        cost = np.zeros(self.iters)
        for i in range(self.iters):
            self.theta = self.theta - (self.alpha/len(x)) * np.sum(x * (x @ self.ftheta.T - y), axis=0)
            self.cost[i] = calc_cost(X, y, theta)

    def print_cost():
        print("Cost: ", self.cost)


    def predict(self, x):
        '''
        Primenjujemo odgovarajuce tezine na linearni polinom
        '''
        b, a = self.w
        return b + a * x
