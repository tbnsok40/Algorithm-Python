# brown = 8
# yellow = 1
#
brown = 24
yellow = 24
#
# def solution(brown, yellow):
#     if yellow == 1:
#         return [3, 3]
#     else:
#         temp = list()
#         for i in range(1, yellow):
#             if yellow % i == 0:
#                 temp.append((int(yellow / i), i))
#         for a, b in temp:
#             if brown == ((a + 2) * (b + 2)) - yellow and a >= b:
#                 return [a+2,b+2]
#
# def solution(brown, yellow):
#     total = brown + yellow
#     for i in range(1, total + 1):
#         if total % i == 0 and yellow == ((int(total / i) - 2) * (i - 2)):
#             return [int(total / i), i]

import math
def solution(brown, yellow):

    # 브라운 가로: 옐로우 가로보다 2 길고
    # 브라운 세로: 옐로우 세로보다 2 길다.
    # 옐로우는 가로와 세로의 곱 ->

    # 결국 브라운 가로 * 세로: 브라운 더하기 옐로우
    sum = brown + yellow # = a*b
    # sum = brown_row * brown_col


# yellow 곱 조합으로 넓이 구할 때, 각각 가로세로 2씩 더해서 sum 이 나오면 그 조합이 답이다.
    for i in range(1, yellow + 1):

        if yellow % i == 0:
            m = yellow // i
            n = i
            print(m, n)
            if (m + 2) * (n + 2) == sum:
                if m >= n:
                    return [m + 2, n + 2]
                else:
                    return [n + 2, m + 2]

print(solution(brown, yellow))
