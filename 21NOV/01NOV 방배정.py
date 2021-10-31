import sys
from itertools import chain

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
classes = [[0, 0] for _ in range(6)]
count = 0

for sex, grade in board:
    classes[grade - 1][sex] += 1

for i in chain(*classes):
    if i > 0:
        b, r = divmod(i, M)
        if b == 0:
            count += 1
        elif b >= 1 and r != 0:
            count += (b + 1)
        else:
            count += b
print(count)

"""
3 3
0 3
1 5
0 6

0: female
1: male
"""
