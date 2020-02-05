from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def __init__(self, lambda_):
        pass

    @abstractmethod
    def fit(self, x, t, mode):
        pass

    @abstractmethod
    def predict(self, x):
        pass
