from algorithms.metrics.R2 import R2


class Metric:

    def __init__(self, y, yy):
        self.y = y
        self.yy = yy

    def eval(self, type):
        """

        :param type: Tip metrike
        :return: Evaluacija
        """
        if type == 'R2':
            r2 = R2(self.y, self.yy)
            return r2.eval()
        elif type == 'RMSE':
            pass




