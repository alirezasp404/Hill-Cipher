import numpy as np


def determinant_gauss_jordan(matrix):

    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError("Input matrix must be a 2D NumPy array.")

    n = matrix.shape[0]
    if n != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")
    
    augmented_matrix = np.hstack((matrix, np.zeros((n, n))))

    det = 1
    for i in range(n):
        # Pivot (largest absolute value in the current column below the diagonal)
        pivot = i
        for j in range(i + 1, n):
            if abs(augmented_matrix[j, i]) > abs(augmented_matrix[pivot, i]):
                pivot = j

        # Check for zero pivot 
        if abs(augmented_matrix[pivot, i]) < 1e-10:
            return 0

        # Swap rows if necessary
        if pivot != i:
            augmented_matrix[[i, pivot], :] = augmented_matrix[[pivot, i], :]
            det *= -1

        # Gauss-Jordan elimination
        det *= augmented_matrix[i, i]
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

    return det


matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 8]
])

determinant = determinant_gauss_jordan(matrix)

print(f"The determinant calculated using gauss-jordan-elimination is: {determinant}")

numpy_det = np.linalg.det(matrix)
print(f"The determinant calculated using NumPy's function is: {numpy_det}")
