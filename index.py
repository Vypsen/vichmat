from gaus.main_elem import mainGaus
from scipy.linalg import solve, det
import numpy as np
import task
from colorama import init, Fore, Style
init()

if __name__ == '__main__':
    
    matrix = task.matrix
    vector = task.vector
    
    if det(matrix) != 0:
        answer = np.round(solve(matrix, vector), 5)
        ansverGaus = np.round(mainGaus(matrix, vector),5)
        
        print(Fore.YELLOW, 'выбор главного элемента:', ansverGaus)
        print(Fore.GREEN, 'питоновский ответ:', answer)
        print(Fore.RED, (answer == ansverGaus).all())
        
    else:
        print(Fore.RED + 'нет решения или их бесконечное количество')
        

        
   