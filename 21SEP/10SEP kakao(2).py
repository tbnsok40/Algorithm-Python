from collections import deque


def change_N_to_K(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    return (rev_base[::-1])


# import math
# 소수 판별 함수(에라토스테네스의 체)
# def primeNumber(n):
#     array = [True for i in range(n + 1)]
#
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if array[i] == True:
#             j = 2
#             while i * j <= n:
#                 array[i * j] = False
#                 j += 1
#     if n == [i for i in range(2, n + 1) if array[i]][-1]:
#         return True
#     else:
#         return False

# 211020101011
def solution(n, k):
    number = change_N_to_K(n, k)
    temp = ''
    candidate = deque()
    for idx, n in enumerate(number):
        if n != 0:
            temp += n
            if idx != len(number) - 1 and (number[idx + 1] == '0'):
                candidate.append(temp)
            if idx == len(number) - 1:
                candidate.append(temp)
    result = []
    for idx, t in enumerate(candidate):
        if idx == 0:
            result.append(t)

        else:
            tt = t[before:].lstrip('0')
            if tt != '1':
                if tt == "":
                    continue
                result.append(tt)
        before = len(t)
    return len(result)


print(solution(437674, 3))
