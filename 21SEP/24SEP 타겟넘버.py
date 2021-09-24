def dfs(idx, numbers, total, target):
    global answer
    if (idx == len(numbers)) and (total == target):
        answer += 1
        return
    if idx == len(numbers):
        return

    dfs(idx + 1, numbers, total + numbers[0], target)
    dfs(idx + 1, numbers, total - numbers[0], target)


def solution(numbers, target):

    global answer
    answer = 0
    dfs(0, numbers, 0, target)

    return answer


print(solution([1, 1, 1, 1, 1], 3))
