from itertools import product


# def solution(numbers, target):
#     temp = [(i, -i) for i in numbers]
#     result = [1 for i in product(*temp) if sum(i) == target]
#     return len(result)


def solution(numbers, target):
    global result

    dfs(0, numbers, target, 0)
    return result


result = 0


def dfs(idx, numbers, target, curr):
    N = len(numbers)
    global result
    if idx == N and curr == target:
        result += 1
        return
    if idx == N:
        return

    dfs(idx + 1, numbers, target, curr + numbers[0])
    dfs(idx + 1, numbers, target, curr - numbers[0]) # 이거 왜 0 이면 안됨...? 어차피 모든 원소 같은거 아냐?


print(solution(numbers=[1, 1, 1, 1, 1], target=3))
