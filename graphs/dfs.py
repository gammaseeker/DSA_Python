def dfs(matrix):
    visited = set()
    stack = [0]
    row = 0
    col = 0
    visited.add(0)
    while stack:
        if matrix[row][col] == 1:
            if col not in visited:
                stack.append(row)
                row = col
                col = 0
                continue
        if col == len(matrix[row]) - 1:
                print(row)
                visited.add(row)
                row = stack.pop()
                col = 0
        else:
            col += 1

def dfs_recursive(matrix, i, j):
    if matrix[i][j] == 1:
        print("{}, {}".format(i, j))
        matrix[i][j] = 0
    else:
        return
    if i - 1 >= 0:
        dfs_recursive(matrix, i-1, j)
    if i + 1 < len(matrix):
        dfs_recursive(matrix, i+1, j)
    if j - 1 >= 0:
        dfs_recursive(matrix, i, j-1)
    if j + 1 < len(matrix[i]):
        dfs_recursive(matrix, i, j + 1)

matrix = [
    [0, 1, 1, 0, 0, 0, 0], 
    [1, 0, 0, 1, 1, 0, 0], 
    [1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 0, 0, 0, 0, 1], 
    [0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0]
]

simple_matrix = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]

rec_matrix = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 0, 1]
]

dfs(simple_matrix)
print("---------------------------")
dfs_recursive(rec_matrix, 0, 0)
