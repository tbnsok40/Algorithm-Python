import sys


def __main__():
    N = int(sys.stdin.readline().rstrip())
    for i in range(max(1, N - 54), N):
        if sum(map(int, str(i))) + i == N:
            print(i)
            exit(0)
    else:
        print(0)


__main__()
