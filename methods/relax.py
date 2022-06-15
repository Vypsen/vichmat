import numpy as np
from scipy.fft import fft

from task import DECIMAL_PLACES


def checkAccuracy(x, x1):
    eps = 10**-DECIMAL_PLACES
    for i in range(x.shape[0]):
        if (abs(x[i] - x1[i]) > eps):
            return False
            
    return True




def calrResultRelaxMethod(matrix, vector, w):
    
    x = np.zeros(matrix.shape[0])
    step = 1
    while(True):
        x1 = np.zeros(matrix.shape[0])
        x0 = x.copy()
        for i in range(matrix.shape[0]):
            x1[i] = (vector[i] - sum(matrix[i][j]*x[j] for j in range(matrix.shape[0])) + matrix[i][i]*x[i])/matrix[i][i]
            x[i] = w*x1[i] + (1 - w)*x0[i]
        print(str(step) + " step: " + str(x1))
        step += 1
        if(checkAccuracy(x1, x0)):
            x = x1.copy()
            break
        x = x1.copy()

    return x

def relax(matrix, vector):

    x = calrResultRelaxMethod(matrix, vector, w = 1.25)
    return x