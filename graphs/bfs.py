import collections

def bfs(matrix):
    visited = set()
    queue = collections.deque([0])
    while queue:
        row = queue.popleft()
        for col in range(0, len(matrix[row])):
            if matrix[row][col] == 1:
                if col not in visited:
                    queue.append(col)
            if col == len(matrix[row]) - 1:
                print(row)
                visited.add(row)

simple_matrix = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]

another_matrix = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0]
]
bfs(simple_matrix) # 0, 1, 2
bfs(another_matrix) # 0, 1, 2, 3, 4, 5, 6, 7, 8
