#!/usr/bin/python3
'''2D matrix'''
def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Driver program
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_2d_matrix(matrix)
for row in matrix:
     print(" ".join(map(str, row)))

