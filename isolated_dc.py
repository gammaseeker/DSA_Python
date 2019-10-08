def dfs(matrix, init_row, all_visited):
    visited = set()
    stack = [init_row]
    visited.add(init_row)
    all_visited.append(init_row)
    row = init_row
    col = 0
    while stack:
        if matrix[row][col] == 1:
            if col not in visited:
                stack.append(row)
                row = col
                col = 0
                continue
        if col == len(matrix[row]) - 1:
            all_visited.append(row)
            visited.add(row)
            row = stack.pop()
            col = 0
        else:
            col += 1
    return visited

def isolated_data_centers(matrix):
    data_centers = []
    all_visited = []
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] == 1:
                if col not in all_visited:
                    data_center_set = dfs(matrix, row, all_visited)
                    data_centers.append(data_center_set)
    return data_centers

matrix = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0]
]

print(isolated_data_centers(matrix))
