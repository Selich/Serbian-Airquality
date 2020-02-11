#!/env/bin/python
from util.data_processing import *
from util.testing_functions import *
from util.helper_functions import *
from util.aqi import AQI
from algorithms.Regression import *
import argparse
import matplotlib.pyplot as plt

gradovi = [ "novisad", "beograd", "uzice", "cacak", "nis" ]

if __name__ == "__main__":

    w = aqi_calc()
    tezine = {
        'NO2 [ug.m-3]': w[0][0],
        'SO2 [ug.m-3]': w[0][1],
        'CO [ug.m-3]': w[0][2]
    }

    atributi = ["SO2 [ug.m-3]","NO2 [ug.m-3]"]

    parser = argparse.ArgumentParser()

    parser.add_argument('--grad', default = '.',
                    help='Podaci o koncentraciji cestica u izabranom gradu.', required=True)
    parser.add_argument('--interval', default = 7,
                    help='Interval koliko dana unapred.')
    parser.add_argument('--stepen', default = 1,
                    help='Stepen regresivnog polinoma.')
    
    args = parser.parse_args()

    grad ,interval, stepen = args.grad, int(args.interval), args.stepen

    yy = find_aqi(grad,atributi)
    yy = predict(grad,interval)

    print(yy)