import sys
from collections import deque


def __main__():
    N = int(sys.stdin.readline().rstrip())
    arr = [[0] * N for _ in range(N)]
    start, end = map(int, input().split())
    queue = deque()
    visited = []
    result = 0
    flag = False
    for _ in range(int(input())):
        x, y = map(int, input().split())
        arr[x - 1][y - 1] = 1
        arr[y - 1][x - 1] = 1
        if x == start or y == start:
            queue.append((y - 1, 1))
            visited.append(y - 1)

    if arr[start - 1][end - 1] == 1:
        print(1)
        exit(0)

    while queue:
        dept, count = queue.popleft()

        for idx in range(N):
            if arr[dept][idx] != 0 and idx == (end - 1):
                print('dept', dept, 'idx', idx, 'count', count, 'queu', queue )
                flag = True
                result = count
                break
                # return count
            if idx in visited:  # visited 엔 이미 방문한 노드인덱스가 있다.
                continue
            if arr[dept][idx] != 0:
                queue.append((idx, count + 1))
                print('q', queue, 'dept', dept, 'idx', idx, 'visi', visited)
                visited.append(idx)
    for a in arr:
        print(a)
    print('v', visited)
    if flag:
        print(result)
    else:
        print(-1)
    return


__main__()

"""
9
8 2
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
"""
