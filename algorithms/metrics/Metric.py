import numpy as np
from algorithms.metrics.R2 import R2


class Metric:

    def __init__(self, y, yy):
        self.y = y
        self.yy = yy

    def mae(self) -> float:
        ret = sum(np.abs(self.y - self.yy))
        return ret

    def mse(self) -> float:
        ret = np.square(self.y - self.yy).mean()
        return ret

    def eval(self, tip: str) -> float:
        """

        :param tip: Tip metrike
        :return: Evaluacija
        """
        if tip == 'R2':
            r2 = R2(self.y, self.yy)
            return r2.eval()
        elif tip.lower() == 'mse':
            return self.mse()
        elif tip.lower() == 'mae':
            return self.mae()





