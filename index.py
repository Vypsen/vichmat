from methods.simpleSelfValue import findMaxSelf
from methods.straightIteration import reverseIteration
from methods.richardson import richardson
from methods.allSelfMean import selfMeanMethodSim

import numpy as np
import task
from scipy.linalg import det, eig
from colorama import init, Fore

init()

if __name__ == '__main__':
    
    matrix = task.matrix
    vector = task.vector

    N = 10
    matrix = np.random.random_integers(-100,100,size=(N,N))
    matrix_symm = (matrix + matrix.T)/2
    print('Матрица:')
    print(matrix_symm)
    w, v = eig(matrix_symm)
    
    if det(matrix_symm) != 0:
        answer = np.array(sorted(selfMeanMethodSim(matrix_symm, 10)))
        w = np.array(sorted(w))
        print('собственные через scipy.linalg:', w)
        print('собственные значения методом вращение Якоби:',answer)
        print('разница между решением scipy.linalg и методом вращение Якоби',w - answer)
    else:
        print(Fore.RED + 'матрица выроженная')
        
        

        
   