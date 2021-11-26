import sys


def __main__():
    N = int(sys.stdin.readline().rstrip())
    origin = N
    result = 0

    while True:
        result += 1
        a = int(N // 10)
        b = int(N % 10)
        c = (a + b) % 10
        N = (b * 10) + c

        if N == int(origin):
            print(result)
            exit(0)


__main__()
