#!/env/bin/python
import argparse
import matplotlib.pyplot as plt
from util.data_processing import *
from algorithms.AQI import *
from algorithms.Regression import *
from algorithms.Metric import *

gradovi = [ "novisad", "beograd", "uzice", "cacak", "nis" ]

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--grad', default = '.',
                    help='Podaci o koncentraciji cestica u izabranom gradu.', required=True)
    parser.add_argument('--interval', default = 7 * 4,
                    help='Interval koliko dana unapred.')
    parser.add_argument('--stepen', default = 1,
                    help='Stepen regresivnog polinoma.')
    
    args = parser.parse_args()

    grad ,interval, stepen = args.grad, int(args.interval), int(args.stepen)

    grad = "nis"
    atributi = ["SO2 [ug.m-3]","NO2 [ug.m-3]"]
    yy = find_and_save_aqi(grad,atributi)
    y = pd.read_csv("./data/aqi_" + grad + ".csv")
    x = np.linspace(0,len(y),len(y))


    yy1 = predict(grad,interval,1)
    yy2 = predict(grad,interval,2)
    yy3 = predict(grad,interval,3)
    plt.scatter(x,y)
    plt.plot(x,yy1)
    plt.plot(x,yy2)
    plt.plot(x,yy3)
    plt.show()
