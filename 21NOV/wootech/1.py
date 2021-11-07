from collections import Counter


def solution(arr):
    arr = Counter(arr)
    max_count = max(Counter(arr).values())
    answer = [0, 0, 0]

    for i in range(1, 4):
        res = max_count - arr[i]
        answer[i - 1] = res
    return answer


arr = [2, 1, 3, 1, 2, 1]
print(solution(arr))
