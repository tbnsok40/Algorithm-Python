import sys
from collections import deque

A, B = sys.stdin.readline().split()
A = int(A)
B = int(B)
count = 0
queue = deque()
# if A == B:
#     print(count)
queue.append([A, count])

while queue:
    value, cnt = queue.popleft()

    if value == B:
        print(cnt)
        exit()

    queue.append([value + 1, cnt + 1])
    queue.append([value - 1, cnt + 1])
    queue.append([value * 2, cnt + 1])


"""

5 17

case 1: x - 1, x + 1
case 2: x * 2

"""
