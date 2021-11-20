import sys
from collections import deque


def square():
    return


def __main__():
    row, col, n = map(int, sys.stdin.readline().rstrip().split())
    board = [[0] * col for _ in range(row)]
    visited = [[False] * col for _ in range(row)]
    queue = deque()
    count = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for _ in range(n):
        x, y, _x, _y = map(int, sys.stdin.readline().rstrip().split())
        for r in range(y, _y):
            for c in range(x, _x):
                board[r][c] = 1
                visited[r][c] = True

    _board = board[::-1]
    _visited = visited[::-1]
    result = []

    for r in range(row):
        for c in range(col):
            if _board[r][c] == 0 and not _visited[r][c]:
                queue.append((r, c))
                _visited[r][c] = True

                _board[r][c] = 1
                individual = 1
                while queue:
                    _r, _c = queue.popleft()
                    for i in range(4):
                        ny = _r + dy[i]
                        nx = _c + dx[i]

                        if ny < 0 or nx < 0 or ny >= row or nx >= col:
                            continue
                        if _board[ny][nx] == 0 and not _visited[ny][nx]:
                            queue.append((ny, nx))
                            _board[r][c] = 1
                            _visited[ny][nx] = True
                            individual += 1
                result.append(individual)
                # count += 1

    # print('individual', individual)
    # for b in _board:
    #     print(b)
    print(len(result))
    result = sorted(result)
    print(' '.join(map(str, result)))


__main__()


"""
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
"""
