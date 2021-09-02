# def solution(N, number):
#     s = [set() for _ in range(8)]
#     for i, x in enumerate(s, start=1):
#         x.add(int(str(N) * i))
#     for i in range(1, 8):  # 최대가 8개 이므로.
#         for j in range(i):
#             for op1 in s[j]:
#                 for op2 in s[i - j - 1]:
#                     # op1, op2 은 같은 숫자들끼리 이미 연산이 된 결과값이다. 우리는 결과가 아니라, 과정을 봐야한다.
#                     s[i].add(op1 + op2)
#                     s[i].add(op1 - op2)
#                     s[i].add(op1 * op2)
#                     if op2 != 0:
#                         s[i].add(op1 // op2)
#         if number in s[i]:
#             answer = i + 1
#             return answer
#     else:
#         return -1
#
