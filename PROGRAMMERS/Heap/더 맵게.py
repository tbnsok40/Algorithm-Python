
scoville = [1, 2, 3, 9, 10, 12]
K = 7

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count =0
    while scoville[0]<K:
        a,b = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, a + b*2)
        count += 1
        if (len(scoville) == 1) and (scoville[0]<K):
            count = -1
            break
    return count


print(solution(scoville,K))