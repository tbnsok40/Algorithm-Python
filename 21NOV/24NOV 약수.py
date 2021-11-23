import sys

# 1
# def __main__():
#     N = int(sys.stdin.readline().rstrip())
#     arr = list(map(int, sys.stdin.readline().split()))
#     if N == 1:
#         return arr[0] ** 2
#     elif N == 2:
#         return arr[0] * arr[1]
#     else:
#         return min(arr) * max(arr)


# 2
def __main__():
    N = int(sys.stdin.readline().rstrip())
    arr = sorted(list(map(int, sys.stdin.readline().split())))
    print(arr[0] * arr[-1])


__main__()
