from gaus.main_elem import mainGaus
from gaus.LU import LuDecomposition
from gaus.optimal import rect_method
from scipy.linalg import solve, det
import numpy as np
import task
from colorama import init, Fore
init()



def output_check(method_text, method):
    answer = np.round(solve(matrix, vector), 7)  
    color = Fore.GREEN if (answer == method).all() else Fore.RED
    print(color, method_text, method)

if __name__ == '__main__':
    
    matrix = task.matrix.astype('float64')
    vector = task.vector.astype('float64')
    
    if det(matrix) != 0:
        
        ansverMainGaus = np.round(mainGaus(matrix, vector), 7)
        ansverOptimalExc = np.round(rect_method(matrix, vector), 7)
        ansverLU = np.round(LuDecomposition(matrix, vector), 7)
            
        output_check('выбор главного элемента:', ansverMainGaus)
        output_check('метод оптимального исключения:', ansverOptimalExc)
        output_check('LU разложение:', ansverLU)
        
    else:
        print(Fore.RED + 'матрица выроженная')
        
        

        
   