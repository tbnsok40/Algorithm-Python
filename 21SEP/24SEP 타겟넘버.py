# def dfs(idx, numbers, total, target):
#     global answer
#     if (idx == len(numbers)) and (total == target):
#         answer += 1
#         return
#     if idx == len(numbers):
#         return
#
#     dfs(idx + 1, numbers, total + numbers[0], target)
#     dfs(idx + 1, numbers, total - numbers[0], target)
#
#
# def solution(numbers, target):
#
#     global answer
#     answer = 0
#     dfs(0, numbers, 0, target)
#
#     return answer

from collections import deque


def solution(numbers, target):
    queue = deque()
    queue.append([0, 0])
    answer = 0
    while queue:
        value, idx = queue.popleft()
        if value == target and idx == len(numbers):
            answer += 1
        if idx == len(numbers):
            continue
        queue.append([value + numbers[idx], idx + 1])
        queue.append([value - numbers[idx], idx + 1])

    return answer


print(solution([1, 1, 1, 1, 1], 3))
