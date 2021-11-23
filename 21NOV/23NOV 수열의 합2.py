import sys
from collections import deque


# def __main__():
#     input = lambda: sys.stdin.readline().rstrip()
#     solid_N, L = map(int, input().split())
#     res = []
#     if L % 2 == 0:
#         l = int((solid_N / L) * 2)
#         for i in range(1, int(l / 2) + 1):
#             if (2 * i + 1) == l:
#                 res.append(i)
#                 res.append(i + 1)
#                 break
#         for i in range(1, 50):
#             res.append(res[0] - 1)
#             res.sort()
#
#             res.append(res[-1] + 1)
#             res.sort()
#
#             if sum(res) > solid_N:
#                 break
#             elif sum(res) == solid_N:
#                 res = sorted(res)
#                 print(res)
#                 exit(0)
#
#
#
#     else:
#         l = (solid_N // L)
#         res.append(l)
#         for i in range(1, 50):
#             res.append(l - i)
#             res.append(l + i)
#             if sum(res) > solid_N:
#                 print(-1)
#                 exit(0)
#                 break
#             elif sum(res) == solid_N:
#                 res = sorted(res)
#                 print(res)
#                 exit(0)


def __main__():
    input = lambda: sys.stdin.readline().rstrip()
    solid_N, L = map(int, input().split())
    results = []

    for length in range(L, 101):
        if length % 2 == 1:
            if solid_N % length == 0:
                median = int(solid_N / length)
                min_result = median - (length - 1) // 2
                if min_result < 0: break
                max_result = median + (length - 1) // 2
                for result in range(min_result, max_result + 1):
                    results.append(result)
                break

        elif length % 2 == 0:
            value = solid_N / length
            print(solid_N % length, value)
            if (value - int(value)) == 0.5:  # 나눈 값의 소수 부분이 0.5일 때.
                min_result = int(value - 0.5)
                if min_result < 0: break
                max_result = int(value + 0.5) + (length // 2 - 1)
                for result in range(min_result, max_result + 1):
                    results.append(result)
                break
    print(results)
    return


__main__()

"""
18 2

연속된 수가, N 을 만들 수 있는지. 
N 을 어케 나눌것인
N 이 10억 까지 치솟으므로, 시간복잡도 고려해야한다. 

연속되어야 한다.
"""
