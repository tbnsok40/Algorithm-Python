n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K = 0
import collections
import heapq
def solution(n, src, dst, edges, K):
    que = collections.defaultdict(list)

    for str, dst, price in edges:
        que[str].append((dst, price)) # dictionary 완료

    # 기준 K에 맞게 하나씩 빼내면서, price 더하기
    Q = [(0, src, K)]
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price

        if k >= 0:
            for v, w in que[node]:
                alt = price + w
                print(alt, v)
                heapq.heappush(Q, (alt, v, k-1))
    return -1
print(solution(n, src, dst, edges, K))