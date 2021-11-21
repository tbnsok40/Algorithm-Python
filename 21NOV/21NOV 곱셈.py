import sys
from collections import deque


def __main__():
    a = int(input())
    b = int(input())

    print(int(str(b)[-1]) * a)
    print(int(str(b)[-2]) * a)
    print(int(str(b)[-3]) * a)
    print(b * a)


__main__()


"""
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
"""
