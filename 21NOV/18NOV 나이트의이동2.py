import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
dx = [2, 2, -2, -2, 1, 1, -1, -1]  # len = 8
dy = [1, -1, 1, -1, 2, -2, 2, -2]
# 이차 배열로 만들고, 최소값만 저장하도록 바꾸자. 여러 경로가 겹치면서 c 값이 무조건적으로 업데이트 되는데, 최소 경로라는게 분명 존재하니 min() 을 사용하여 업뎃하자.

for _ in range(N):
    result = []
    length = int(sys.stdin.readline().rstrip())
    _a, _b = map(int, sys.stdin.readline().split())
    x, y = map(int, sys.stdin.readline().split())

    # if _a == x and _b == y:
    #     print(0)
    #     continue

    visited = [[False] * length for _ in range(length)]
    visited[_a][_b] = True
    queue = deque() # 초기화 해주지 않으면 이전의 queue 와 겹칠 수 있다.
    queue.append((_a, _b, 0))

    while queue:
        a, b, c = queue.popleft()
        if a == x and b == y:
            print(c)
            break
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            # if nx == x and ny == y:
            #     break

            if nx < 0 or length <= nx or ny < 0 or length <= ny:
                continue

            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            queue.append((nx, ny, c + 1))


    # for i in range(8):
    #     nx = x + dx[i]
    #     ny = y + dy[i]
    #     if -1 < nx < length and -1 < ny < length:
    #         result.append(visited[nx][ny])
    # print(min(result) + 1)

"""
2
4
0 0
0 0
4
1 1
1 1
"""