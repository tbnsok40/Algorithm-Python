from itertools import permutations, combinations
import heapq


def solution(n, m, k):
    a = ["a"] * (n) + ["b"] * (m + 2)
    permutations_heap = []
    for case in set(permutations(a, n+2 + m)):
        heapq.heappush(permutations_heap, case)

    if len(permutations_heap) < k:
        return ""
    for _ in range(k - 1):
        ab = heapq.heappop(permutations_heap)
        print(''.join(ab))

    result = heapq.heappop(permutations_heap)

    return ''.join(result)

    # for _ in range(k - 1):
    #     heapq.heappop(permutations_heap)
    # result = heapq.heappop(permutations_heap)
    # return ''.join(result)

    # res = 1
    # for i in range(1, 4 + 1):
    #     res *= i
    # print(res)
    # return


# 시간초과
# def solution(n, m, k):
#     bracket_dict = {'a': '(', 'b': ')'}
#     a = ["a"] * n + ["b"] * m
#
#     permutations_set = []
#     for case in set(permutations(a, n + m)):
#         permutations_set.append(''.join(case))
#     permutations_set.sort()
#
#     answer = ""
#     for r in permutations_set[k - 1]:
#         answer += bracket_dict[r]
#
#     return answer

# 시간초과2
# def solution(n, m, k):
#     a = ["("] * n + [")"] * m
#     permutations_heap = []
#     for case in set(permutations(a, n + m)):
#         heapq.heappush(permutations_heap, case)
#
#     for _ in range(k - 1):
#         heapq.heappop(permutations_heap)
#     result = heapq.heappop(permutations_heap)
#     return ''.join(result)

n = 2
m = 2
k = 5

print(solution(n, m, k))
