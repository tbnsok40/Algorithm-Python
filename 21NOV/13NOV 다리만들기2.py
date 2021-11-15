import sys
from collections import deque

N = int(input())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
numberIsland = 1
queue = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = sys.maxsize
for r in range(N):
    for c in range(N):
        if board[r][c] == 1 and visited[r][c] == 0:
            queue.append((r, c))
            visited[r][c] = 1
            board[r][c] = numberIsland

            while queue:
                r, c = queue.popleft()
                for i in range(4):
                    nx = c + dx[i]
                    ny = r + dy[i]
                    if -1 < nx < N and -1 < ny < N and board[ny][nx] == 1 and visited[ny][nx] == 0:
                        # 각 대륙마다 번호를 부여
                        board[ny][nx] = numberIsland
                        queue.append((ny, nx))
                        visited[ny][nx] = 1
            numberIsland += 1


def bfs(z):
    global answer
    v_queue = deque()
    unvisited = [[-1] * N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if board[row][col] == z:
                v_queue.append((row, col))
                unvisited[row][col] = 0
    while v_queue:
        row, col = v_queue.popleft()
        for j in range(4):
            _nx = col + dx[j]
            _ny = row + dy[j]

            if _nx < 0 or _nx >= N or _ny < 0 or _ny >= N:
                continue

            if board[_ny][_nx] > 0 and board[_ny][_nx] != z:
                print(unvisited[row][col], board[_ny][_nx], z)
                answer = min(answer, unvisited[row][col])
                return

            if board[_ny][_nx] == 0 and unvisited[_ny][_nx] == -1:
                unvisited[_ny][_nx] = unvisited[row][col] + 1
                v_queue.append((row, col))

        # if board[dr][dc] != 0 and unvisited[dr][dc] == 0:
        #     v_queue.append((dr, dc))
        #     while v_queue:
        #         r, c = v_queue.popleft()
        #         for i in range(4):
        #             nx = c + dx[i]
        #             ny = r + dy[i]
        #             if -1 < nx < N and -1 < ny < N and board[ny][nx] == 0 and unvisited[ny][nx] == 0:
        #                 # 여기에 들어왔다는 건 테두리라는 뜻, 여길 못 들어왔
        #                 unvisited[ny][nx] = unvisited[r][c] + 1
        #                 v_queue.append((ny, nx))


for i in range(1, numberIsland):
    bfs(i)

print(answer)

# 대륙마다 고유 번호 가진다 => 다른 번호 가진 것들 끼리 이어본다.

"""
https://www.acmicpc.net/problem/2146
1 <= N <= 100
대륙이 3개든 5개든, 하나의 가장 짧은 다리만 완성시키고 리턴하면 된다.
어느곳에서 출발한다 할 때, 다른 대륙과 맞닿아야지, 자기가 속한 대륙과 닿으면 안된다.
다른 대륙인지는 어떻게 판단할 것인가. 
1. 섬이 몇개인지 구한다.
2. 섬중 하나를 선택해, 섬의 크기를 늘려가며, 다른 섬에 닿는 거리를 구한다.
3. 과정 2를 전체 섬에 대해 구한 후 최소값을 출력

10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0

"""
