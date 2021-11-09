import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
for _ in range(T):

    C, R, N = map(int, sys.stdin.readline().split())
    board = [[0 for _ in range(C)] for _ in range(R)]
    visited = [[0 for _ in range(C)] for _ in range(R)]
    for _ in range(N):
        c, r = map(int, sys.stdin.readline().split())
        board[r][c] = 1
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] == 1 and visited[r][c] == 0:
                visited[r][c] = 1
                queue.append((r, c))
                count += 1
                while queue:
                    nr, nc = queue.popleft()
                    for i in range(4):
                        nx = nc + dx[i]
                        ny = nr + dy[i]
                        if -1 < nx < C and -1 < ny < R and board[ny][nx] == 1 and visited[ny][nx] == 0:
                            queue.append((ny, nx))
                            visited[ny][nx] = 1

    print(count)



