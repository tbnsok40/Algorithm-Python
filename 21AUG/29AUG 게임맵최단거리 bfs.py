from collections import deque


def solution(maps):
    row = len(maps)
    column = len(maps[0])
    matrix = [[- 1 for _ in range(column)] for _ in range(row)]

    queue = deque()
    queue.append([0, 0])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    matrix[0][0] = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < column and 0 <= ny < row and maps[ny][nx] == 1 and matrix[ny][nx] == -1:
                # matrix[ny][nx] = maps[y][x] + 1
                matrix[ny][nx] = matrix[y][x] + 1
                queue.append([ny, nx])

    return matrix[row - 1][column - 1]


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(maps))
