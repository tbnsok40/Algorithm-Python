import heapq
def solution(scoville, K):

    # 힙으로 만들고
    heapq.heapify(scoville)
    count = 0
# 정확성은 all pass, 효율성은 all fail
#     while min(scoville) < K: # min(scoville)은 O(N)
#         try:
#             temp = heapq.heappop(scoville) + heapq.heappop(scoville)*2
#             heapq.heappush(scoville, temp)
#             count += 1
#         except IndexError:
#             return -1

    while scoville[0] < K:
        temp = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, temp)
        count +=1
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return count


scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville, K))