import numpy as np

def determinant(matrix):
    dimension = matrix.shape[0]
    
    if dimension == 1:
        return matrix[0, 0]
    if dimension == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    # Find row and column with the most zeros
    zero_counts_rows = np.sum(matrix == 0, axis=1)
    zero_counts_cols = np.sum(matrix == 0, axis=0)
    
    # Determine whether to use row or column for expansion
    if np.max(zero_counts_rows) >= np.max(zero_counts_cols):
        use_row = True
        index = np.argmax(zero_counts_rows)
    else:
        use_row = False
        index = np.argmax(zero_counts_cols)

    det = 0
    for i in range(dimension):
        if use_row:
            if matrix[index, i] == 0:
                continue
            sub_matrix = np.delete(np.delete(matrix, index, axis=0), i, axis=1)
            sign = (-1) ** (index + i)
            sub_det = determinant(sub_matrix)
            det += sign * matrix[index, i] * sub_det
        else:
            if matrix[i, index] == 0:
                continue
            sub_matrix = np.delete(np.delete(matrix, i, axis=0), index, axis=1)
            sign = (-1) ** (i + index)
            sub_det = determinant(sub_matrix)
            det += sign * matrix[i, index] * sub_det

    return det

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 8]
])

result = determinant(matrix)
print(f"The determinant calculated using Laplace expansion is: {result}")

numpy_det = np.linalg.det(matrix)
print(f"The determinant calculated using NumPy's function is: {numpy_det}")