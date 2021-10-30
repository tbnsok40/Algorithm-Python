import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    # if y == N - 1 and x == M - 1:
    #     print(board[N - 1][M - 1])
    #     return board[N - 1][M - 1]
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (-1 < ny < N) and (-1 < nx < M) and board[ny][nx] == 1:
                board[ny][nx] = board[y][x] + 1
                queue.append((ny, nx))
                # dfs(ny, nx)
    # for b in board:
    #     print(b)
    return board[N - 1][M - 1]


print(dfs(0, 0))

"""

4 6
101111
101010
101011
111011

"""

