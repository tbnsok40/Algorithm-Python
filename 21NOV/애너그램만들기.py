import sys
from collections import deque
a = deque(sorted(list(sys.stdin.readline().rstrip())))
b = deque(sorted(list(sys.stdin.readline().rstrip())))
result = 0

for _ in range(len(a)):
    pops = a.popleft()
    if pops not in b:
        result += 1
        pass
    else:
        a.append(pops)

for _ in range(len(b)):
    pops = b.popleft()
    if pops not in a:
        result += 1
        pass
    else:
        b.append(pops)
for idx, i, in enumerate(a):
    if a.count(i) != b.count(i):
        result += abs(a.count(i) - b.count(i))


print(result)
"""
abcd
bccde
"""