import numpy as np
from enum import Enum

# SO2 [ug.m-3],O3 [ug.m-3],NO2 [ug.m-3],NOX [ug.m-3],CO [mg.m-3],NO [ug.m-3],V [m/s],dd [°],P [mb],t [°C],Rh [%]
constraints = {
    "AQI": [0,50, 100, 150, 200, 300, 400, 500],
    "CO [mg.m-3]": [0,4.4, 9.4, 12.4, 15.4, 30.4, 40.4, 50.4],
    "SO2 [ug.m-3]": [0,35, 75, 185, 304, 604, 804, 1004],
    "NO2 [ug.m-3]": [0,53, 100, 360, 649, 1249, 1649, 2049],
    "PM25": [0,12, 35.4, 55.4, 150.4, 250.4, 350.4, 500.4]
}


class AQI():
    def __init__(self, conc = 0, gas="AQI"):
        self.conc = conc
        for i in range(0,len(constraints[gas]) - 1):
            if constraints[gas][i] < self.conc <= constraints[gas][i+1]:
                self.min = i
                self.max = i + 1
                break

        aqi = (self.conc - constraints[gas][self.min]) * (constraints["AQI"][self.max] - constraints["AQI"][self.min])
        aqi /= (constraints[gas][self.max] - constraints[gas][self.min])
        aqi += constraints["AQI"][self.min]
        self.aqi = aqi

    def get_value(self):
        return self.aqi



