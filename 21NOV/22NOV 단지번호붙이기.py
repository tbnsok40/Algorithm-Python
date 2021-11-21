import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def __main__():
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = []

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for r in range(N):
        for c in range(N):
            if board[r][c] == 1 and visited[r][c] == 0:
                queue = deque()
                queue.append((r, c))
                visited[r][c] = 1
                count = 1
                while queue:
                    y, x = queue.popleft()
                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]

                        if ny < 0 or nx < 0 or ny >= N or nx >= N:
                            continue

                        if board[ny][nx] == 1 and visited[ny][nx] == 0:
                            queue.append((ny, nx))
                            visited[ny][nx] = 1
                            count += 1
                result.append(count)

    print(len(result))
    for x in sorted(result):
        print(x)
    return


__main__()

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
