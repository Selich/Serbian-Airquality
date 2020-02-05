#!/env/bin/python
from util.data_processing import *
from util.testing_functions import *
from util.helper_functions import *

# SO2 [ug.m-3],O3 [ug.m-3],NO2 [ug.m-3],NOX [ug.m-3],CO [mg.m-3],NO [ug.m-3],V [m/s],dd [°],P [mb],t [°C],Rh [%]

if __name__ == "__main__":
    ds_name = input("Upisite dataset: ")
    data = read_data(ds_name)
    test_aqi(data, "CO [mg.m-3]")
    test_prediction(data, "CO [mg.m-3]")

