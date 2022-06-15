import numpy as np
from task import DECIMAL_PLACES

def gradient(matrix, vector):
    eps = 10** -DECIMAL_PLACES
    x = np.zeros(matrix.shape[0])

    step = 0
    while True:
        f = np.dot(matrix, x) - vector
        step += 1
        print(str(step) + " step: " + str(x))

        if max(abs(f)) < eps:
            return x

        r = -f
        lambd = (np.dot(r, r)) / (np.dot(np.dot(r, matrix), r))
        x -= np.dot(lambd, f)
        

        

        

