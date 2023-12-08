def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter elements for row {i + 1} separated by space: ").split()))
        if len(row) != cols:
            print("Error: Number of elements doesn't match the number of columns.")
            return None
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def subtract_matrices(matrix1, matrix2):
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def display_matrix(matrix):
    for row in matrix:
        print(row)

rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

print("\nEnter elements for the first matrix:")
matrix1 = input_matrix(rows1, cols1)
print("\nEnter elements for the second matrix:")
matrix2 = input_matrix(rows2, cols2)

if matrix1 is not None and matrix2 is not None:
    print("\n1. Addition of matrices:")
    display_matrix(add_matrices(matrix1, matrix2))

    print("\n2. Subtraction of matrices:")
    display_matrix(subtract_matrices(matrix1, matrix2))

    print("\n3. Multiplication of matrices:")
    display_matrix(multiply_matrices(matrix1, matrix2))

    print("\n4. Transpose of the first matrix:")
    display_matrix(transpose_matrix(matrix1))
    
    print("\n5. Transpose of the second matrix:")
    display_matrix(transpose_matrix(matrix2))