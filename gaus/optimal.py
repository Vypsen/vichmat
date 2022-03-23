def rect_method(matrix, vector):
    
    for row in range(matrix.shape[0]):    
        main_elem = matrix[row][row]
          
        matrix[row] /= main_elem
        vector[row] /= main_elem
                    
        for index_row in range(row - 1, -1, -1): 
            matrix[index_row] -= matrix[row]*matrix[index_row][row]
            vector[index_row] -= vector[row]*matrix[index_row][row]
            
        if row + 1 == matrix.shape[0]:
            return vector
        
        for index_row in range(row, -1, -1): 
            matrix[row + 1] -= matrix[index_row]*matrix[row + 1][index_row]        
            vector[row + 1] -= vector[index_row]*matrix[row + 1][index_row] 
    