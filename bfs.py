def bfs(matrix):
    visited = set()
    queue = []
    visited.add(0)
    for i in range(0, len(matrix[0])):
        if matrix[0][i] == 1:
            queue.append(i)

    row = queue.pop(0)
    col = 0

    while queue:
        if matrix[row][col] == 1:
            if col not in visited:
                queue.append(col)
        if col == len(matrix[row]) - 1:
            print(row)
            visited.add(row)
            row = queue.pop(0)
            col = 0
        else:
            col += 1

simple_matrix = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]

bfs(simple_matrix)
