from contextlib import AbstractAsyncContextManager
import numpy as np
from numpy import linalg as la

from methods.inverse import inverse, createInverse
from methods.main_elem import mainGaus
from task import DECIMAL_PLACES


def reverseIteration(matrix, eps):
    x = np.array([1]*matrix.shape[0])
    x0 = np.array([2]*matrix.shape[0])
    alpha = np.max(x)
    new_alpha = np.max(x0)
    lam = 1/alpha
    iteration = 0

    while (la.norm(1/alpha-1/new_alpha)) >= eps:
        alpha = new_alpha
        v = x/alpha
        x = np.round(inverse(matrix, v), DECIMAL_PLACES)
        
        new_alpha = np.amax((x))
        lam = 1/alpha
        iteration += 1
        print('iter', iteration, lam)


    return lam