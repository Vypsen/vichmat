import numpy as np
from numpy import linalg as la

def findMaxSelf(matrix, eps):
    iteration = 0

    x = np.array([1]*matrix.shape[0])
    y = np.dot(matrix, x)
    lam = y*x
    new_x = y/la.norm(y)

    while(la.norm(new_x*np.sign(lam) - x) > eps):
        x = new_x
        y = np.dot(matrix, x)
        lam = np.dot(y,x)
        new_x = y/la.norm(y)
        iteration += 1
        print('iter', iteration, lam)

    return lam

