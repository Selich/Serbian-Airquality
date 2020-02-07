import numpy as np
from algorithms import Model
from scipy import linalg


class Regression():

    def __init__(self, lambda_=1.):
        self.lambda_ = lambda_
        self.w = None

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

    def predict(self, x):
        '''
        Primenjujemo odgovarajuce tezine na linearni polinom
        '''
        b, a = self.w
        return b + a * x
