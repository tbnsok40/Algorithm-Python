import sys
import heapq


N = int(sys.stdin.readline().rstrip())
heap = []
count = 0

for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline().rstrip()))

while heap:
    if len(heap) == 1:
        break

    total = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, total)
    count += total

print(count)

"""

덧셈 작업이 발생하면, 그 결과를 어떤 스택 같은곳에 반드시 기록해둔다.
동시에, 덧셈의 결과를 또 다른 숫자와 더하도록 준비해야한다. 
그리하여 어떤 큐나 스택의 길이가 하나가 되면, 더이상 덧셈을 할 수 없으므로, 연산을 끝낸다. 

"""
