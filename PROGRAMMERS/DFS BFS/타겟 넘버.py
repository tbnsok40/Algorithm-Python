# answer = 0
# def DFS(idx, numbers, target, curr_value):
#     global answer
#
#     N = len(numbers)
#     if (idx == N and curr_value == target):
#         answer += 1
#         return
#     if (idx == N):
#         return
#     DFS(idx+1, numbers, target, curr_value+numbers[idx])
#     DFS(idx+1, numbers, target, curr_value-numbers[idx])
#
# def solution(numbers, target):
#     global answer
#     DFS(0, numbers, target, 0)
#     return answer
#
# numbers = [2,2,2,2,2]
# target = 6
# print(solution(numbers,target))

# beautiful
# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)
numbers = [1,1,1,1,1]
target = 3

from itertools import product
def solution(numbers, target):
    l = [(x,-x) for x in numbers] # this
    s = list(map(sum, product(*l))) # and this two line is like binary tree maker.
    return s.count(target)

print(solution(numbers, target))
