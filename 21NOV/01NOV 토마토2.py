from collections import deque
from itertools import chain

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for row in range(n):
    for col in range(m):
        if board[row][col] == 1:
            queue.append((row, col))

while queue:
    y, x = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 1)1을 추가했다 2)큐에도 넣어야한다.
        if -1 < nx < m and -1 < ny < n and (board[ny][nx] == 0):
            board[ny][nx] = board[y][x] + 1
            queue.append((ny, nx))

for i in (chain(*board)):
    if i == 0:
        print(-1)
        exit()

else:
    print(max(chain(*board)) - 1)






"""
6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""