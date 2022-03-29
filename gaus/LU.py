import numpy as np
def createLU(m):
    
    u = np.zeros((m.shape[0], m.shape[0]))
    l = u.copy()

    # копируем первую строчку
    u[0] = m[0].copy()
    
    # первый столбец l
    for i in range(1, m.shape[0]):
        l[i][0] = m[i][0]/u[0][0]
        

    for i in range(1, m.shape[0]):
        for j in range(i, m.shape[0]):
            u[i][j] = m[i][j] - sum([l[i][k] * u[k][j] for k in range(i)])
            l[j][i] = (m[j][i] - sum([l[j][k] * u[k][i] for k in range(i)]))/u[i][i]
    return l, u
            
            
            
def result(l, u, v):
    x = np.zeros(u.shape[0])
 
    for i in range(u.shape[0]):
        x[i] = v[i] - sum([l[i][j]*x[j] for j in range(i)])

    n = u.shape[0] - 1

    for i in range(n + 1):
        x[n - i] = (x[n-i] - sum([u[n-i][n-p]*x[n-p] for p in range(i)]))/u[n - i][n - i]
  
    return x

def LuDecomposition(matrix, vector):
    matrix = matrix.copy()
    vector = vector.copy()
    
    l, u = createLU(matrix)
    return result(l, u, vector)