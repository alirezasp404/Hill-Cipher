def determinant(matrix):
    dimension = len(matrix)
    
    if dimension == 1:
        return matrix[0][0]
    if dimension == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Find row and column with the most zeros
    zero_counts_rows = [row.count(0) for row in matrix]
    zero_counts_cols = [sum(row[i] == 0 for row in matrix) for i in range(dimension)]
    
    # Determine whether to use row or column for expansion
    if max(zero_counts_rows) >= max(zero_counts_cols):
        use_row = True
        index = zero_counts_rows.index(max(zero_counts_rows))
    else:
        use_row = False
        index = zero_counts_cols.index(max(zero_counts_cols))

    det = 0
    for i in range(dimension):
        if use_row:
            if matrix[index][i] == 0:
                continue
            sub_matrix = [row[:i] + row[i+1:] for row in (matrix[:index] + matrix[index+1:])]
            sign = (-1) ** (index + i)
            sub_det = determinant(sub_matrix)
            det += sign * matrix[index][i] * sub_det
        else:
            if matrix[i][index] == 0:
                continue
            sub_matrix = [row[:index] + row[index+1:] for row in (matrix[:i] + matrix[i+1:])]
            sign = (-1) ** (i + index)
            sub_det = determinant(sub_matrix)
            det += sign * matrix[i][index] * sub_det

    return det

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 8]
]

result = determinant(matrix)
print(f"The determinant calculated using Laplace expansion is: {result}")

# Note: We can't use numpy's linalg.det function here, so we'll omit that comparison