# from collections import deque
#
#
# def solution(N, number):
#     calc = ["+", "-", "//", "*"]
#     # 5, N 만 사용
#     # 숫자를 붙이는 경우, 사칙연산이 하나씩 나오는 경우
#     # N_queue = deque([N] * 8)
#     # N의 갯수에 따라 만들 수 있는 경우를 짜본다.
#
#     """
#     N의 갯수를  for 문으로
#     """
#     # 1. [ SET x 8 ] 초기화
#     s = [set() for x in range(8)]
#     print(s)
#     # 2. 각 set마다 기본 수 "N" * i 수 초기화
#     for i, x in enumerate(s, start=1):
#         print(i, x)
#         x.add(int(str(N) * i))
#     print(s)
#     # def spliting(n, calc):
#     #     while len(n) >= 2:
#     #         a = n[0]
#     #         b = spliting(n[1:], calc)
#     #
#     # n[0] + spliting(n[1:], calc)
#     # n[0] - spliting(n[1:], calc)
#     # n[0] * spliting(n[1:], calc)
#     # n[0] // spliting(n[1:], calc)
#
#     return
#
#

def solution(N, number):

    # N : 5, 작은 개수부터 올려보내다가, number 랑 맞는 조건 있으면 리턴한다.
    # sets = [str(N) * i for i in range(1, 9]
    s = [set() for x in range(8)]
    for i, x in enumerate(s, start = 1):
        x.add(int(str(N) * i))

    for i in range(1, 8):  # 최대가 8개 이므로.
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:

                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
                    print(i, s[i])
                print(' ')
        if number in s[i]:
            answer = i + 1
            return answer
    else:
        return -1


N, number = 5, 12


print(solution(N, number))
