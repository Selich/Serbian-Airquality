import numpy as np
from scipy import linalg
from collections import OrderedDict
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

class PolynomialRegression(object):

    def __init__(self, x, y):     
        self.x = x
        self.y = y      
    
    def norm(self,data):
        ret = (data - np.mean(data))/(np.max(data) - np.min(data))
        return ret
        
    def hipoteza(self, theta, x):
        h = theta[0]
        for i in np.arange(1, len(theta)):
            h += theta[i]*x ** i        
        return h        
        
    def cost(self, x, y, theta):
        m = len(y)  
        h = self.hipoteza(theta, x)
        errors = h-y
        
        return (1/(2*m))*np.sum(errors**2) 
        
    def fit(self, stepen, tol = 10**-3, numIters = 20, alpha = 0.01):
        # WORKS
        x_train, x_test, y_train, y_test = train_test_split(self.x,self.y)

        X = np.c_[np.ones(self.x.shape[0]), self.norm(self.x)]
        for i in np.arange(2, stepen+1):                
            X2 = np.c_[np.ones(self.x.shape[0]), self.norm(self.x ** i)]
            X = np.append(X, X2, axis=1)
            X = np.delete(X, i, 1)


        self.y = self.y.reshape((len(self.y), )) 
        self.y = self.norm(self.y)

        m = len(self.x)
        theta = np.zeros(stepen + 1)           
        costs = []
        for i in range(numIters):
         
            h = self.hipoteza(theta, self.x)       
            errors = h-self.y
            theta += -alpha * (1/m)*np.dot(errors, X)
            cost = self.cost(self.x, self.y, theta)
            costs.append(cost)         

            if tol > cost:
                break
            
        self.costs = costs
        self.numIters = numIters
        self.theta = theta        

        return self
        
    def plot_predicted(self):
        plt.figure()
        plt.scatter(self.x, self.y, s = 30, c = 'b') 
        line = self.theta[0] #y-intercept 
        for i in np.arange(1, len(self.theta)):            
            line += self.theta[i] * self.x ** i 

        plt.plot(self.x, line, label = ''.join(label_holder))        
        plt.title('Polynomial Fit: Stepen ' + str(len(self.theta)-1))
        plt.xlabel('x')
        plt.ylabel('y') 
        plt.legend(loc = 'best')
        plt.show()

    def plot_cost(self):
        plt.figure()
        plt.plot(np.arange(1, self.numIters+1), self.costs, label = r'$J(\theta)$')
        plt.xlabel('Iterations')
        plt.ylabel(r'$J(\theta)$')
        plt.legend(loc = 'best')
        plt.show()

