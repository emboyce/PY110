'''
goes backwards

9
[2][1] > [1][1]
[1][1] > [2][1]

7
[2][2] > [2][1]
[1][2] > [2][2]

5
[2][3] > [3][1]
[1][3] > [3][1]

the lowest row becomes the highest column
1, col > ?, max
the original column becomes the new row
1, col > col, max



00 01 02 > xx xx 03
10 11 12 > xx xx 13
20 21 22 > xx xx 23

'''
def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transpose = [[matrix[row][column] for row in range(rows)] 
                                      for column in range(columns)]

    return transpose

def rotate90even(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    rotate = [[None for row in range(rows)]
                        for column in range(columns)]
    
    for column in range(columns - 1, -1, -1):
        for row in range(rows):
            rotate[row][column] = matrix[columns - column - 1][row]

    return rotate

def rotate90(matrix):
    transp_matrix = transpose(matrix)
    for row in transp_matrix:
        row.reverse()

    return transp_matrix

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)