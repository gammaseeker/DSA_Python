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

dfs(simple_matrix)
