import numpy as np
from methods.inverse import dot, createInverse
import numpy.linalg as lin
import math

# проекция
def proj(a, b):
    return (dot(a, b) / dot(b, b)) * b

def createQ(matrix):
    n = matrix.shape[0]

    q = matrix.copy()

    for i in range(n):
        # применяем алгоритм ортогонализации Грама – Шмидта
        q_1 = np.zeros(n)
        q_1 = sum(proj(matrix[:, i], q[:, j]) for j in range(i))
        q[:, i] = matrix[:, i] - q_1
        # нормируем
        q[:, i] /= math.sqrt(dot(q[:, i], q[:, i]))
        
    return q


def createR(q, matrix):
    return dot(createInverse(q), matrix)


def solveTriangular(matrix, y):
    n = matrix.shape[0]
    x = np.zeros(n, dtype=float)

    for i in range(n):
        for j in range(i):
            y[n-1-i] -= matrix[n-1-i][n-1-j]*x[n-1-j]
        x[n-1-i] = y[n-1-i]/matrix[n-1-i][n-1-i]

    return x


def QR(matrix, vector):
    q = createQ(matrix)
    r = createR(q, matrix)

    y = dot(np.transpose(q), vector)

    x = solveTriangular(r, y)

    return x


















































































































































































































from numpy import dot



