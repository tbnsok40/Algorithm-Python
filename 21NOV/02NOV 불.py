import sys
from collections import deque
from itertools import chain

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
days = 0
j_queue = deque()
f_queue = deque()

# find J position
for row in range(R):
    for col in range(C):
        if board[row][col] == 'J':
            j_queue.append((row, col))
        elif board[row][col] == "F":
            f_queue.append((row, col))

count = 0
while f_queue:
    row, col = f_queue.popleft()
    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]
        if (-1 < ny < R) and (-1 < nx < C) and board[ny][nx] != '#':
            board[ny][nx] = "F"
            f_queue.append((ny, nx))
while j_queue:
    j_row, j_col = j_queue.popleft()

    for i in range(4):
        jy = j_row + dy[i]
        jx = j_col + dx[i]
        if jy >= R or jy < 0 or jx < 0 or jx >= C:
            print(count + 1)
            # print(board)
            exit()

        if board[jy][jx] == ".":
            board[jy][jx] = "J"
            j_queue.append((jy, jx))
            count += 1

# 불을 먼저 확산시키고, 불, 벽 좌표에 따라 지훈이를 이동시키자,
"""
4 4
####
#JF#
#..#
#..#
"""
