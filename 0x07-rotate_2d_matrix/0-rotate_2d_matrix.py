#!/usr/bin/python3
'''D matrix'''
def get_matrix_from_user():
    try:
        num_rows = int(input("Enter the number of rows: "))
        num_cols = int(input("Enter the number of columns: "))

        matrix = []
        for i in range(num_rows):
            row = input(f"Enter row {i+1} (space-separated values): ")
            row_values = [int(x) for x in row.split()]
            matrix.append(row_values)  

        return matrix
    except EOFError:
        print("No input provided. Using default values.")
        
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

def rotate_2d_matrix(matrix):
    return [list(reversed(i)) for i in zip(*matrix)]

matrix = get_matrix_from_user()
print("Original matrix:")
for row in matrix:
    print(row)

rotated_matrix = rotate_2d_matrix(matrix)
print("\nRotated matrix:")
for row in rotated_matrix:
    print(row)

