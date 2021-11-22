import sys
from collections import deque
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def __main__():
    N, K, = map(int, input().split())
    result = []
    queue = deque(i for i in range(1, N + 1))

    while queue:
        for _ in range(K - 1):
            queue.append(queue.popleft())
        result.append(queue.popleft())

    print("<", end='')
    for i in range(len(result)):
        if i == len(result) - 1:
            print(result[i], end='>')
            exit(0)
        print(result[i], end=', ')


__main__()

"""
7 3
"""
