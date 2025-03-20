matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

'''
in: matrix of 3
out: transposed matrix of 3
1, 5, 8 >
1
5
8
4 7 2 >
x 4
x 7
x 2

run through the rows of the matrix
for each row, assign each value to the appropriate spot in the new matrix
    row-th spot in each row
    [1][1], [1][2], [1][3] > [1][1], [2][1], [3][1]
    [2][1], [2][2], [2][3] > [1][2], [2][2], [3][2]
    [3][1], [3][2], [3][3] > [1][3], [2][3], [3][3]
'''

def transpose1(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    output = [[matrix[row][column] for row in range(rows)]
                                    for column in range(columns)
            ]
    
    print(output)
    return output

def transpose0(matrix):
    output = []
    for row in range(len(matrix)):
        sub_matrix = []
        for column in range (len(matrix[0])):
            sub_matrix.append(matrix[column][row])
        output.append(sub_matrix)

    print(output)
    return output

'''new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])''' 

def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    output = []

    for column in range(columns):
        new_row = [matrix[row][column] for row in range(rows)]
        output.append(new_row)

    return output


# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)