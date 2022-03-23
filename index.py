from gaus.main_elem import mainGaus
from gaus.optimal import rect_method
from scipy.linalg import solve, det
import numpy as np
import task
from colorama import init, Fore
init()

if __name__ == '__main__':
    
    matrix = task.matrix.astype('float64')
    vector = task.vector.astype('float64')

    if det(matrix) != 0:
        ansverOptimalExc = np.round(rect_method(matrix, vector), 7)
        answer = np.round(solve(matrix, vector), 7)
        ansverMainGaus = np.round(mainGaus(matrix, vector), 7)
        
        print(Fore.YELLOW, 'выбор главного элемента:', ansverMainGaus)
        print(Fore.YELLOW, 'метод оптимального исключения:', ansverOptimalExc)

        print(Fore.GREEN, 'питоновский ответ:', answer)
        print(Fore.RED, (answer == ansverMainGaus).all())
        print(Fore.RED, (answer == ansverOptimalExc).all())

    else:
        print(Fore.RED + 'матрица выроженная')
        

        
   