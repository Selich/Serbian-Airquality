import numpy as np
from algorithms import Model


class R2:

    def __init__(self, y, yy):
        self.y = y
        self.yy = yy

    def ss_residual(self):
        """
        Suma od kvadrata razlike y i y^
        :param y: Realna vrednost
        :param yy: Izracunata vrednost pomocu modela
        :return: Rezidual
        """
        ret = sum((self.y - self.yy) ** 2)
        return ret

    def ss_total(self):
        """
        Suma od kvadrata razlike y i srednje vrednosti y
        :param y: Realna vrednost
        :param yy: Srednja ( mean ) realne vrednosti vrednost
        :return:
        """
        ret = sum((self.y - np.mean(self.y)) ** 2)
        return ret

    def eval(self):
        """
        R-kvadrat (R2) se koristi za objasnjenje
            koliko dobro izabrane promenljive
            objasnjavaju promenljivost u zavisnim promenljivim

        :return: Koeficijent korelacije
        """
        ret = 1 - (float(self.ss_residual())) / self.ss_total()
        return ret



