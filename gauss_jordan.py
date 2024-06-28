def determinant_gauss_jordan(input_matrix):
    n = len(input_matrix)
    # Create a copy of the matrix to avoid modifying the original
    matrix = [row[:] for row in input_matrix]
    
    det = 1
    for i in range(n):
        # Find the pivot (largest absolute value in the column)
        pivot = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[pivot][i]):
                pivot = j
        
        # If the pivot is zero, the determinant is zero
        if matrix[pivot][i] == 0:
            return 0
        
        # Swap rows if necessary
        if pivot != i:
            matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
            det *= -1
        
        # Gauss-Jordan elimination
        det *= matrix[i][i]
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]
    
    return det

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = determinant_gauss_jordan(matrix)
print(f"Determinant of the matrix: {result}")