import sys
from collections import deque


N = int(input())
count = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    queue = deque(list(word))
    stack = []
    while queue:
        pops = queue.popleft()
        if not stack:
            stack.append(pops)
        else:
            if stack[-1] == pops:
                stack.pop()
            else:
                stack.append(pops)

    if not stack:
        count += 1

print(count)
