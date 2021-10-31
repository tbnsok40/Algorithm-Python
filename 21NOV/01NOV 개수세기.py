import sys

N = map(int, sys.stdin.readline().rstrip())
a = [int(x) for x in sys.stdin.readline().rstrip().split()]
M = int(sys.stdin.readline().rstrip())
print(a.count(M))

"""
11
1 4 1 2 4 2 4 2 3 4 4
2
"""