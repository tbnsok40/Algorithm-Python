import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()
max_area = -1
count = 0
for r in range(N):
    for c in range(M):
        # if board[r][c] == 1:
        area = 1
        queue.append([r, c])
        visited = []
        while queue:
            y, x = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if (0 <= nx <= M - 1) and (0 <= ny <= N - 1) and (board[y][x] == 1) and ([ny, nx] not in visited):
                    if board[ny][nx] == 1:
                        queue.append([ny, nx])
                        visited.append([ny, nx])
                        area += 1
            # print(queue)
        if area >= max_area:
            max_area = area

print(max_area, count)

queue = deque([0, 0])  # 일차원 배열
queue2 = deque()
queue2.append([0, 0])  # 이차원 배열
print(queue, queue2)
print(queue.popleft(), queue2.popleft())
"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 1
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

visited 를 만들자. 
전체 for 문으로 돌리더라도, 이미 visited 에 있는 것은 제끼자. 
대각선 이어지는것도 막아야한다. 
"""
