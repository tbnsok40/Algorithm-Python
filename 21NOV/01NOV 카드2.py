import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()
if N == 1:
    print(1)
    sys.exit()
for i in range(1, N + 1):
    queue.append(i)
while len(queue) != 2:
    queue.popleft()
    queue.append(queue.popleft())
queue.popleft()
print(queue[-1])
