def transpose_matrix(matrix):
    # turn row index to col index
    # turn col index to row index
    for i in range(0, len(matrix)):
        for j in range(i+1, len(matrix[i])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    return matrix
matrix = [1,2,3],[4,5,6],[7,8,9]
print(transpose_matrix(matrix))