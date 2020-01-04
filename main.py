
import pandas as pd
from algorithms import ridge
from util.helper_functions import  read_data

def main():
    df = read_data("beograd")
    print(df.head())






if __name__ == "__main__":
    main()
