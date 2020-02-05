from util.data_processing import *
from util.testing_functions import *

if __name__ == "__main__":
    data = read_data("beograd")
    test_prediction(data)
