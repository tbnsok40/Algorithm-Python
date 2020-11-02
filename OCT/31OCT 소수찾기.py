# 시간 초과
# def solution(n):
#     answer = []
#     for i in range(2,n+1):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             answer.append(i)
#     return len(answer)

# 시간 초과
# def solution(n):
#     answer = []
#     for i in range(2, n + 1):
#         if sosu(i):
#             answer.append(i)
#     return len(answer)
# def sosu(p):
#     for j in range(2, p):
#         if p % j == 0:
#             break
#     else:
#         return True

# 시간초과
# def solution(n):
#     answer = [2]
#     for i in range(3, n + 1):
#         for j in answer:
#             if i % j == 0:
#                 break
#         else:
#             answer.append(i)
#     return len(answer)




# print(solution(10))


