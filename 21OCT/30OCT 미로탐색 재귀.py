import sys


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]


def dfs(y, x):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # if y == N - 1 and x == M - 1:
    #     print(board[N - 1][M - 1])
    #     return board[N - 1][M - 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (-1 < ny < N) and (-1 < nx < M) and board[ny][nx] == 1:
            board[ny][nx] = board[y][x] + 1
            dfs(ny, nx)

    for b in board:
        print(b)

    return board[N - 1][M - 1]


print(dfs(0, 0))

"""

4 6
101111
101010
101011
111011


[3, 2, 0, 8, 9, 0]
[2, 3, 0, 7, 8, 0]
[3, 4, 5, 6, 7, 8]
[4, 5, 6, 7, 0, 9]
"""

