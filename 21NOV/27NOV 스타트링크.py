import sys
from collections import deque


def __main__():
    F, S, G, U, D, = map(int, sys.stdin.readline().rstrip().split())

    if U == 0 and D == 0:
        print("use the stairs")
        exit(0)
    if S == G:
        print(0)
        exit(0)

    queue = deque()
    ori_visited = [0] * (F + 1)
    ori_visited[S] = 1
    queue.append((S, 0, ori_visited))
    direction = [U, -D]
    arrive = False
    while queue:
        curr, count, visited = queue.popleft()

        for i in direction:
            new_curr = curr + i  # curr += i ... 이걸 건드리면 안됐네.
            n_count = count + 1

            if new_curr == G:
                arrive = True
                print(n_count)
                exit(0)

            if 0 >= new_curr or 0 >= new_curr or new_curr > F or new_curr > F:
                continue

            if visited[new_curr] != 1:
                visited[new_curr] = 1
                queue.append((new_curr, n_count, visited))
    if not arrive:
        print("use the stairs")


__main__()
