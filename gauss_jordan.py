def determinant_gauss_jordan(input_matrix):
  
  matrix_len = len(input_matrix)
  if matrix_len != len(input_matrix[0]):
    raise ValueError("Input matrix must be square.")

  matrix = [[row[i] for i in range(matrix_len)] for row in input_matrix]

  det = 1
  for i in range(matrix_len):
    # Partial pivoting (find largest absolute value in the current column below the diagonal)
    pivot = i
    for j in range(i + 1, matrix_len):
      if abs(matrix[j][i]) > abs(matrix[pivot][i]):
        pivot = j

    # Check for zero pivot
    if abs(matrix[pivot][i]) < 1e-10:
      return 0

    # Swap rows if necessary
    if pivot != i:
      matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
      det *= -1

    # Gauss-Jordan elimination
    det *= matrix[i][i]
    for j in range(i + 1, matrix_len):
      factor = matrix[j][i] / matrix[i][i]
      matrix[j][i] = 0  # Explicitly set pivot element to zero for clarity
      for k in range(i + 1, matrix_len):
        matrix[j][k] -= factor * matrix[i][k]

  return det

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 8]
]

result = determinant_gauss_jordan(matrix)
print(f"Determinant of the matrix: {result}")
