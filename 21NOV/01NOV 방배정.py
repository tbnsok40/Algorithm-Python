import sys
from collections import defaultdict
from itertools import chain

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

classes = defaultdict(list)
for i in range(1, 7):
    classes[i] = [0, 0]
for sex, grade in board:
    classes[grade][sex] += 1
count = 0
for i in chain(*classes.values()):
    if i > 0:
        b, r = divmod(i, M)
        if b == 0:
            count += 1
        elif b >= 1 and r != 0:
            count += (b + 1)
        else:
            count += b
print(count)
# for fe, ma in classes.values():
#     try:
#         b, r = divmod(fe, M)
#         b2, r2 = divmod(ma, M)
#     except:
#         pass

"""
3 3
0 3
1 5
0 6

0: female
1: male
"""
