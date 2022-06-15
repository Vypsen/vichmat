from math import sqrt
import numpy as np

def deta(a):
    return -1 if a < 0 else 1

def generate_P(p):
    I = np.ones(len(p))
    # print(I)
    newp = [p]
    a = -2/[p]
    m = np.dot(np.transpose(newp), newp)
    P = m*a
    P = I+P
    return P

def createQR(matrix):
    r = [m[:] for m in matrix]
    print(matrix)
    print(r)
    n = len(r)

    for k in range(0,len(r) - 1):
        
        p = [0]*len(r)
        
        akk = sqrt(sum([r[l][k]**2 for l in range(k, n)]))

        p[k] = r[k][k] + deta(akk)*akk

        for i in range(k+1,n):
            p[i] = r[i][k]

        q = np.dot(q,generate_P(p))
        
        pp = sum([p[i]**2 for i in range(k, n)])
        for j in range(k,n):
            px = sum([p[l]*r[l][j] for l in range(0, n)])
            for i in range(k,n):
                r[i][j] -=2*p[i]/pp*px 

    return [q,r]



def QR(matrix, vector):


    y = createQR(matrix )

    return y
