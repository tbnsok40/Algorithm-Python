import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-work for work in works]
    heapq.heapify(works)

    # for i in range(n):
    #
    #     heapq._heapify_max(works)
    #     works[0] -= 1
    for i in range(n):
        work = heapq.heappop(works)
        work += 1
        if work > 0:
            work = 0
        heapq.heappush(works, work)
    return sum(map(lambda x: x**2, works))

works = [3,4,3]
n = 4
print(solution(n, works))

# 효율성 털린 풀이법
def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-work for work in works]
    heapq.heapify(works)

    for i in range(n):
        heapq._heapify_max(works)
        works[0] -= 1

    return sum(map(lambda x: x**2, works))

## heapq -> heapq.heapify : O(n)
## heapq -> heapq.heappush or heapq.heappop : O(log(n))


