def determinant_gauss_jordan(matrix):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Input matrix must be a list of lists.")
    
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Input matrix must be square.")
    
    augmented_matrix = [row + [0] * n for row in matrix]
    
    det = 1
    for i in range(n):
        # Pivot (largest absolute value in the current column below the diagonal)
        pivot = i
        for j in range(i + 1, n):
            if abs(augmented_matrix[j][i]) > abs(augmented_matrix[pivot][i]):
                pivot = j
        
        # Check for zero pivot
        if abs(augmented_matrix[pivot][i]) < 1e-10:
            return 0
        
        # Swap rows if necessary
        if pivot != i:
            augmented_matrix[i], augmented_matrix[pivot] = augmented_matrix[pivot], augmented_matrix[i]
            det *= -1
        
        # Gauss-Jordan elimination
        det *= augmented_matrix[i][i]
        for j in range(i + 1, n):
            factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            for k in range(n * 2):
                augmented_matrix[j][k] -= factor * augmented_matrix[i][k]
    
    return det

