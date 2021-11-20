import sys


def __main__():
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if b >= c:
        print(-1)
        exit(0)
    print((a // (c - b)) + 1)


__main__()
