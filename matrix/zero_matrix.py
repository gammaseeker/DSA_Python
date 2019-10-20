def zero_matrix(matrix):
    # Check if top row has 0
    row_zero = False
    for col in range(0, len(matrix[0])):
        if matrix[0][col] == 0:
            row_zero = True

    # Check if first col has 0
    col_zero = False
    for row in range(0, len(matrix)):
        if matrix[row][0] == 0:
            col_zero = True

    # Look for zeros and mark them in first row,col
    if len(matrix) > 1 and len(matrix[0]) > 1:
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

    # Insert the zeros
    if len(matrix) > 1 and len(matrix[0]) > 1:
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
    if row_zero:
        for col in range(0, len(matrix[0])):
            matrix[0][col] = 0 
    if col_zero:
        for row in range(0, len(matrix)):
            matrix[row][0] = 0

test1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
test2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

zero_matrix(test1)
print(test1)

zero_matrix(test2)
print(test2)
