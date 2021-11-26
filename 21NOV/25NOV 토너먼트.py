import sys


def calculate(num):

    if num // 2 == num / 2:
        return num // 2
    else:
        return (num // 2) + 1


def __main__():
    N, a, b = map(int, sys.stdin.readline().rstrip().split())
    # first, second = (a, 0), (b, 0)
    count = 0
    while True:
        count += 1
        a = calculate(a)
        b = calculate(b)
        if a == b:
            return count


print(__main__())
