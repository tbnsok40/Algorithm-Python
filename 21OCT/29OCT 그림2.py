import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()
num_list = []

for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            area = 1
            queue.append([r, c])
            board[r][c] = 0  # 여기를 초기화 시켜주는게 중요하네 중복되지 않도록.

            while queue:
                y, x = queue.popleft()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if (0 <= nx <= M - 1) and (0 <= ny <= N - 1) and (board[ny][nx] == 1):
                        queue.append([ny, nx])
                        board[ny][nx] = 0  # 여기'도' 초기화 시켜준다.
                        area += 1
            num_list.append(area)

if len(num_list):
    print(len(num_list))
    print(max(num_list))
else:
    print(len(num_list))
    print(0)

"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

visited 를 만들자. 
전체 for 문으로 돌리더라도, 이미 visited 에 있는 것은 제끼자. 
대각선 이어지는것도 막아야한다. 
"""
