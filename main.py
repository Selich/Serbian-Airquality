#!/env/bin/python
from util.data_processing import *
from util.testing_functions import *
from util.helper_functions import *
import matplotlib.pyplot as plt

# SO2 [ug.m-3],O3 [ug.m-3],NO2 [ug.m-3],NOX [ug.m-3],CO [mg.m-3],NO [ug.m-3],V [m/s],dd [°],P [mb],t [°C],Rh [%]

gradovi = [
    "novisad", "beograd", "uzice", "cacak", "nis"
]


degrees = [i for i in range(1,7)]



def populate_aqi(data: pd.DataFrame):
    aqi_series = pd.Series(index=data.index)
    names = list(data.columns)
    max_aqi = 0
    for idx, row in data.iterrows():
        for name in names:
            try:
                temp_aqi = AQI(row[name], name)
                if temp_aqi > max_aqi:
                    max_aqi = temp_aqi
            except expression as identifier:
                pass
        aqi_series.loc[idx] = max_aqi
    
    return aqi_series
        
        
def mse(y,yy,theta):
    tobesummed = np.power(((y @ theta.T)-yy),2)
    return np.sum(tobesummed)/(2 * len(y))

def gradient_descent(X,y,theta,iters,alpha):
    cost = np.zeros(iters)
    for i in range(iters):
        theta = theta - (alpha/len(X)) * np.sum(X * (X @ theta.T - y), axis=0)
        cost[i] = mse(X, y, theta)
    
    return theta,cost

def norm(data):
    data = (data - data.mean()) / data.std()
    return data


def mutl():
    beograd = read_data("novisad")
    nis = read_data("nis")
    poznati_atributi = ["SO2 [ug.m-3]", "NO2 [ug.m-3]", "CO [mg.m-3]"]

    my_data = beograd[poznati_atributi]
    my_data = norm(my_data)
    my_data.drop(my_data.tail(1).index,inplace=True) 
    X = my_data.iloc[:,0:1]
    ones = np.ones([X.shape[0],1])
    X = np.concatenate((ones,X),axis=1)
    y = my_data.iloc[:,2:3].values 
    theta = np.zeros([1,3])
    alpha = 0.01
    iters = 1000
    
    w,cost = gradient_descent(X,y,theta,iters,alpha)
    print(w)

    finalCost = mse(X,y,w)

    print(finalCost)
    X = nis[poznati_atributi[0:2]]

    ser = pd.Series(index=nis.index)
    # for i in range(0,len(X)):
    #     ser[i] = X.loc[i] @ w.T


    print(ser)
    plt.plot(ser)
    plt.show()

    

def aqi_calc():
    beograd = read_data("novisad")


    

if __name__ == "__main__":








    
    

