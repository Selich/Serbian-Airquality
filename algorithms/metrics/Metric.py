import numpy as np
import math


class Metric:

    def __init__(self, y, yy):
        self.y = y
        self.yy = yy

    def mae(self):
        ret = sum(np.abs(self.y - self.yy)) / len(self.y)
        return ret

    def rmse(self):
        ret = math.sqrt(sum(np.square(self.y - self.yy)) / len(self.y))
        return ret

    def r2(self):
        y = self.y
        yy = self.yy
        ret = sum((yy-sum(y)/len(y))**2) / sum((y - sum(y)/len(y))**2)

        return ret

    def eval(self, tip: str) -> float:
        """

        :param tip: Tip metrike
        :return: Evaluacija
        """
        if tip == 'r2':
            ret = self.r2()
            return ret
        elif tip.lower() == 'rmse':
            ret = self.rmse()
            return ret
        elif tip.lower() == 'mae':
            ret = self.mae()
            return ret
