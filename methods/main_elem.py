import numpy as np

def mainGaus(matrix, vector):
    matrix = matrix.copy()
    vector = vector.copy()
    
    index_main_elem = np.unravel_index(np.argmax(abs(matrix)), matrix.shape)
    main_elem = matrix[index_main_elem]
    main_line = matrix[index_main_elem[0]].copy()
    main_vector = vector[index_main_elem[0]]
    if main_elem == 0:
        return [0]*matrix.shape[1]
        
    for i in range(matrix.shape[0]):
        multiplier = matrix[(i,index_main_elem[1])]/main_elem
        matrix[i] -= main_line*multiplier 
        vector[i] -= main_vector*multiplier
        
    answer = mainGaus(matrix, vector)  
    
    root = main_vector/main_elem - sum(list(main_line[i]/main_elem * answer[i] 
                                            for i in range(len(main_line.tolist()))))
    
    answer[index_main_elem[1]] = root
    return answer
