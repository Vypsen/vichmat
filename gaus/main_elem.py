import numpy as np

def mainGaus(matrix, vector):
    index_main_elem = np.unravel_index(np.argmax(abs(matrix)), matrix.shape)
    main_elem = matrix[index_main_elem]
    main_line = matrix[index_main_elem[0]]
    main_vector = vector[index_main_elem[0]]
    
    if len(vector) == 1:
        first_root = [0]*matrix.shape[1]
        first_root[index_main_elem[1]] = vector[index_main_elem[0]]/matrix[index_main_elem]
        
        return first_root
    
    new_matrix = np.delete(matrix, index_main_elem[0], 0)
    new_vector = np.delete(vector, index_main_elem[0], 0)
    
    for i in range(new_matrix.shape[0]):
        multiplier = abs(new_matrix[(i,index_main_elem[1])]/main_elem)
        new_matrix[i] += main_line*multiplier 
        new_vector[i] += main_vector*multiplier
     
    answer = mainGaus(new_matrix, new_vector)
    
    answer[index_main_elem[1]] = (
        vector[index_main_elem[0]]/matrix[index_main_elem]) - (
        sum(list(alpha/main_elem * answer[matrix.tolist()[index_main_elem[0]].index(alpha)] 
            for alpha in matrix.tolist()[index_main_elem[0]])))
        
    return(answer)
