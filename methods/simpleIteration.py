import numpy as np

def checkAccuracy(x, x0):
    eps = 10** -8
    for i in range(x.shape[0]):
        if (abs(x[i] - x0[i]) > eps):
            return False
            
    return True


def calrResultSimpleIteration(matrix, vector):
    
    x = np.zeros(matrix.shape[0])
    step = 1
    while(True):
        x1 = np.zeros(matrix.shape[0])
        for i in range(matrix.shape[0]):
            x1[i] = (vector[i] - sum(matrix[i][j]*x[j] for j in range(matrix.shape[0])) + matrix[i][i]*x[i])/matrix[i][i]
        print(str(step) + " step: " + str(x1))
        step += 1
        if(checkAccuracy(x1, x)):
            x = x1.copy()
            break
        x = x1.copy()

    return x


def calrResultMethodSeidel(matrix, vector):

    x = np.zeros(matrix.shape[0])
    step = 1
    while(True):
        x1 = np.zeros(matrix.shape[0])
        x0 = x.copy()
        for i in range(matrix.shape[0]):
            x1[i] = (vector[i] - sum(matrix[i][j]*x[j] for j in range(matrix.shape[0])) + matrix[i][i]*x[i])/matrix[i][i]
            x[i] = x1[i]
        print(str(step) + " step: " + str(x1))
        step += 1
        if(checkAccuracy(x1, x0)):
            x = x1.copy()
            break
        x = x1.copy()

    return x


def simpleIteration(matrix, vector):

    x = calrResultSimpleIteration(matrix, vector)
    return x

def methodSeidel(matrix, vector):

    x = calrResultMethodSeidel(matrix, vector)
    return x