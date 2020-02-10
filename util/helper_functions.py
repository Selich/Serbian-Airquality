import numpy as np
import pandas as pd

def loss_fn(X, Y, beta):
    return np.linalg.norm(np.matmul(X, beta) - Y)**2

def regularizer(beta):
    return np.linalg.norm(beta)

def objective_fn(X, Y, beta, lambd):
    return loss_fn(X, Y, beta) + lambd * regularizer(beta)

def mse(X, Y, beta):
    return (1.0 / X.shape[0]) * loss_fn(X, Y, beta).value

def print_menu():
    print("Izaberite opciju")
    print("\t1. Ucitajte dataset")
    print("\t2. Testirajte regresiju")
    print("\t3. Testirajte AQI")
    print("\n")

def menu():
    option = -1
    flag = 0
    while(option != '0'):
        if flag : print("\nAktivan file: " + ds_name)
        print_menu()
        option  = input()
        if option == '1':
            ds_name = input("\nUpisite naziv geografske lokacije: ")
            try:
                data = read_data(ds_name)
                flag = 1
                print("\nPodaci su ucitani!")
            except:
                print("\nNije nadjena lokacija")

        elif option == '2':
            if(data is None): 
                print("\nNije aktiviran dataset")
                break
            obelezije = input("Izaberite obelezije: ")
            test_prediction(data,obelezije)
        elif option == '3':
            if(data is None): 
                print("\nNije aktiviran dataset")
                break
            test_aqi(data)
        elif option == '0':
            return
        else:
            print("\nOdaberite validnu opciju")
    