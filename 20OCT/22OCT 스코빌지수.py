scoville = [1, 2, 3, 9, 10, 12]

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while len(scoville)>1:
        count += 1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        if K <= scoville[0]:
            return count
    return -1

# 아래 코드가 구조상/맥락적으로 깔끔
# try ~ except 구문

def solution(scoville, K):
    heapq.heapify(scoville) # 힙 구조 만들어주기
    count = 0
    while scoville[0]<K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
            count += 1
        except IndexError:
            return -1
    return count
