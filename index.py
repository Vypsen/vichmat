from gaus.main_elem import mainGaus
from scipy.linalg import solve, det
import numpy as np
import task
from colorama import init, Fore
init()

if __name__ == '__main__':
    
    matrix = task.matrix.astype('float64')
    vector = task.vector.astype('float64')

    
    if det(matrix) != 0:
        answer = np.round(solve(matrix, vector), 7)
        ansverGaus = np.round(mainGaus(matrix, vector),7)
        
        print(Fore.YELLOW, 'выбор главного элемента:', ansverGaus)
        print(Fore.GREEN, 'питоновский ответ:', answer)
        print(Fore.RED, (answer == ansverGaus).all())
        
    else:
        print(Fore.RED + 'нет решения или их бесконечное количество')
        

        
   