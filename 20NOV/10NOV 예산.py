def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop() # pop()은 리스트[-1]원소부터 빠지는 것, pop(0)가 맨 앞 원소 pop
    return len(d)


# (추가) 정수제곱근판별
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