from util.data_processsing import *
from util.testing_functions import *


def main():
    data = read_data("beograd")
    test_prediction(data)


if __name__ == "__main__":
    main()
