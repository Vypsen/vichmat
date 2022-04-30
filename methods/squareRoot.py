from cmath import sqrt
import numpy as np

def createS(matrix):
    size = matrix.shape[0]
    matrixS = np.zeros((size, size), dtype=complex)
    matrixS[0] = matrix[0] / sqrt(matrix[0][0])
    matrixS[0][0] = sqrt(matrix[0][0])

    for i in range(size):
        matrixS[i][i] = sqrt(matrix[i][i] - sum((matrixS[k][i])**2 for k in range(i)))    
        for j in range(i, size):
            matrixS[i][j] = (matrix[i][j] - sum((matrixS[k][i]*matrixS[k][j]) for k in range(i)))/matrixS[i][i]
            
    print(matrixS)
    return matrixS


def getAnsver(s, v):
    size = s.shape[0]
    y = np.zeros(size, dtype=complex)
    
    for i in range(len(s)):
        y[i] = (v[i] - sum([s[k][i]*y[k] for k in range(i)]))/s[i][i]
    
    return y

def solveTriangular(matrix, y):
    n = matrix.shape[0]
    x = np.zeros(n, dtype=complex)

    for i in range(n):
        for j in range(i):
            y[n-1-i] -= matrix[n-1-i][n-1-j]*x[n-1-j]
        x[n-1-i] = y[n-1-i]/matrix[n-1-i][n-1-i]

    return x
            
def squareRoot(matrix, vector):
    matrix = matrix.copy()
    vector = vector.copy()

    matrixS = createS(matrix)
    y = getAnsver(matrixS, vector)
    x = solveTriangular(matrixS, y)
    
    return x
























    def transpose(m):
        if(type(m[0]) != list):
        temp = [[i for i in m]]

    else:
        if(len(m[0]) == 1):
            temp = [[r[0] for r in m]]
        else:
            temp = [[ 0 for i in range(len(m))] for j in range(len(m[0]))]
            for i in range(len(m)): 
                for j in range(len(m[0])):
                    temp[j][i] = m[i][j]

    return temp



    def mul(m,a):
        if(type(m) != list):
        return None

    if(type(m) == list and type(m[0]) != list):
        temp = [r*a for r in m]

    elif(type(m[0][0]) != list):
        temp = [r[:] for r in m]
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                temp[i][j] *= a

    return temp