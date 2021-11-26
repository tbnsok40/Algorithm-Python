import sys


def __main__():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    count = 0
    for i in range(N):
        j = i
        while True:
            j += 1
            if sum(arr[i:j]) == M:
                count += 1
                break
            if sum(arr[i:j]) > M:
                break
            if j >= len(arr):
                break
    print(count)


__main__()
