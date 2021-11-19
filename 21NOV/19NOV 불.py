import sys
from collections import deque


def __main__():
    N = int(sys.stdin.readline().rstrip())
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for _ in range(N):
        flag = True
        queue = deque()
        f_queue = deque()

        C, R = map(int, sys.stdin.readline().rstrip().split())
        board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
        visited = [[False] * C for _ in range(R)]

        f_board = [[0] * C for _ in range(R)]
        f_visited = [[False] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if board[r][c] == "*":
                    f_queue.append((r, c))
                    f_visited[r][c] = True
                    # f_visited.append([r, c])
                    continue

                if board[r][c] == "@":
                    if r == 0 or c == 0 or r == R - 1 or c == C - 1:
                        flag = False
                    board[r][c] = 0
                    queue.append((r, c))
                    continue
        if not flag:
            print(1)
            continue

        while f_queue:
            r, c = f_queue.popleft()
            for i in range(4):
                ny = r + dy[i]
                nx = c + dx[i]
                if ny >= R or ny < 0 or nx >= C or nx < 0:
                    continue
                if board[ny][nx] == "#":
                    continue
                if f_board[ny][nx] == 0 and f_visited[ny][nx] == False:  # [ny, nx] not in f_visited:
                    f_board[ny][nx] = f_board[r][c] + 1
                    f_queue.append((ny, nx))

        while queue:
            r, c = queue.popleft()
            for i in range(4):
                ny = r + dy[i]
                nx = c + dx[i]
                if ny >= R or ny < 0 or nx >= C or nx < 0:
                    continue
                if board[ny][nx] == "#":
                    continue
                if board[ny][nx] == "." and visited[ny][nx] == False:
                    if f_board[ny][nx] == 0:
                        board[ny][nx] = board[r][c] + 1
                        queue.append((ny, nx,))
                    else:
                        if f_board[ny][nx] > (board[r][c] + 1):
                            # if ny == 3 and nx == 4:
                            # print(f_board[ny][nx] , board[r][c])

                            board[ny][nx] = board[r][c] + 1
                            queue.append((ny, nx,))

        # for b in board:
        #     print(b)
        # for b in f_board:
        #     print(b)
        result = []
        for r in range(R):
            if r == 0 or r == R - 1:
                for c in range(C):
                    if board[r][c] not in ["#", "*", "."]:  # != "#" and board[r][c] != ".":
                        result.append(board[r][c])
                    if board[r][c] not in ["#", "*", "."]:
                        # if board[r][c] != "#" and board[r][c] != ".":
                        result.append(board[r][c])
            else:
                for c in [0, C - 1]:
                    if board[r][c] not in ["#", "*", "."]:
                        # if board[r][c] != "#" and board[r][c] != ".":
                        result.append(board[r][c])
                    if board[r][c] not in ["#", "*", "."]:
                        # if board[r][c] != "#" and board[r][c] != ".":
                        result.append(board[r][c])

        if result:
            print(int(min(result)) + 1)
        else:
            print("IMPOSSIBLE")


__main__()

"""
1
7 4
###.###
#.....#
#@....#
*######


1
5 7
...#*
..##.
##.#.
#@...
##.#.
..##.
...#*
"""
