import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
ori_board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
ori_visited = [[0] * N for _ in range(N)]
rg_visited = [[0] * N for _ in range(N)]
rg_board = []
for i in ori_board:
    rg = ''.join(i).replace('G', 'R')
    rg_board.append(list(rg))

ori_queue = deque()
rg_queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ori_count = 0
rg_count = 0


def bfs(queue, visited, board, count):
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                queue.append((r, c))
                while queue:
                    _r, _c = queue.popleft()
                    for i in range(4):
                        ny = _r + dy[i]
                        nx = _c + dx[i]
                        if -1 >= ny or ny >= N or -1 >= nx or nx >= N:
                            continue

                        if board[_r][_c] == board[ny][nx] and visited[ny][nx] == 0:
                            queue.append((ny, nx))
                            visited[ny][nx] = -1
                count += 1
    return count


ori_count = bfs(ori_queue, ori_visited, ori_board, ori_count)
rg_count = bfs(rg_queue, rg_visited, rg_board, rg_count)
print(ori_count, end=' ')
print(rg_count)
