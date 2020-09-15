scoville = [12,2,3,9,10,1]
K = 7
# 리스트의 최소 원소가 K보다 큰지 확인
# 크지 않다면 합성과정 +1
# sum(합성과정) = answer
import heapq
def solution(scoville, K):
    # 힙구조 사용해도 좋을 듯
    # 최소 힙 구현
    heap = scoville
    heapq.heapify(heap) # 힙 구조 만들어주기
    answer = 0
    # 반복문 한번 돌 때마다 answer += 1
    while heap[0]<K:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, (first + second*2))
        answer += 1
        # 예외처리
        if (len(heap) == 1) and (heap[0]<K):
            answer = -1
            break
    ############### 위의 코드는 아래처럼 try except으로 확 줄일 수 있다.
    while scoville[0] < K:
        try:
            heappush(scoville, heappop(scoville) + heappop(scoville)*2)
        except IndexError:
            return -1
        count += 1
    ###########################################
    return answer
print(solution(scoville,K))