import sys
from collections import deque
from itertools import chain

M, N = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
days = 0
queue = deque()


# 여기 로직 문제
def find_zero():
    for row in range(N):
        for col in range(M):
            count = 0
            for i in range(4):
                nx = col + dx[i]
                ny = row + dy[i]

                # 범위 초과하는 순간 여기 로직 못타서 바로 FAlse 가 나온다 . 그래서 무조건 False 가 나오는 상황인거임
                if board[row][col] == 0 and (-1 < nx < M) and (-1 < ny < N) and board[ny][nx] == -1:
                    count += 1
            if count == 4:
                return False
            elif 2 <= count <= 3:
                if col + 1 >= M or col - 1 < 0 or row + 1 >= N or row - 1 < 0:
                    return False
                else:
                    return True
            else:
                return True


def recursive(day):
    # if not find_zero():
    #     print('here')
    #     return -1

    global days

    if 0 not in chain(*board):
        days = day
        return

    # 1 첫 탐색(1 좌표)
    for row in range(N):
        for col in range(M):
            if board[row][col] == 1:
                queue.append((row, col))

    while queue:
        row, col = queue.popleft()
        for i in range(4):
            ny = row + dy[i]
            nx = col + dx[i]

            if (-1 < ny < N) and (-1 < nx < M) and board[ny][nx] == 0:
                board[ny][nx] = 1
    day += 1
    recursive(day)


if not find_zero():
    print(-1)
    sys.exit()
else:
    recursive(0)
print(days)
# if days != 0:
#     print(days)
# else:
#     print(-1)

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

-1 인 경우 : 반복했을 때 day는 달라졌는데, queue 는 변함이 없고, board 에 0 이 존재할 때.
"""
