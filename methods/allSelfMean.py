import numpy as np

def sgn(num):
    	return 1 if num > 0 else -1

def findMaxNdInd(matrix):
	mi, mj = 0,1
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if(i != j and abs(matrix[i][j]) > abs(matrix[mi][mj])):
				mi, mj = i, j
	return [mi, mj]


def selfMeanMethodSim(matrix, p):
    tau = np.array([10**(-(i+1)) for i in range(p)])

    matrix = np.array([r[:] for r in matrix])
    step = 0
    for p in tau:
        i, j = findMaxNdInd(matrix)

        while(abs(matrix[i][j]) >= p): 
            d = ((matrix[i][i] - matrix[j][j])**2 + 4*(matrix[i][j])**2)**0.5
            c = (0.5*( 1 + abs(matrix[i][i] - matrix[j][j])/d))**0.5
            s = sgn(matrix[i][j]*(matrix[i][i] - matrix[j][j])) * (0.5*(1 - abs(matrix[i][i] - matrix[j][j])/d))**0.5

            new_m = np.array([ r[:] for r in matrix])

            new_m[i][j] = new_m[j][i] = 0

            for k in range(len(matrix)):
                if(k == i or k == j):
                    continue
                new_m[k][i] = new_m[i][k] = c * matrix[k][i] + s* matrix[k][j]
                new_m[k][j] = new_m[j][k] = -s * matrix[k][i] + c* matrix[k][j]
            
            new_m[i][i] = c**2*matrix[i][i] + 2*c*s*matrix[i][j] + s**2*matrix[j][j]

            new_m[j][j] = s**2*matrix[i][i] - 2*c*s*matrix[i][j] + c**2*matrix[j][j]

            matrix = new_m

            i, j = findMaxNdInd(matrix)
            step += 1
    return np.array([matrix[i][i] for i in range(len(matrix))])