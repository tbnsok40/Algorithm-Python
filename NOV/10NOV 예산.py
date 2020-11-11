def solution(d, budget):

    if sum(d) == budget:
        return len(d)

# d = [1,3,2,5,4]
# budget = 9
#
# d = [2,2,3,3]
# budget = 10
# print(solution(d,budget))


# import math
# def solution(n):
#     if math.sqrt(n) % 1 != 0:
#         return -1
#     else:
#         return int((math.sqrt(n) + 1)**2)
#
#     if int(math.sqrt(n)) == math.sqrt(n):
#         return (int(math.sqrt(n))+1)**2
#     else:
#         return -1
# print(solution(121))