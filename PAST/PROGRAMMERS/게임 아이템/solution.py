# 리더님 피드백
# 나는 if문이 for문 밖에 있어도 된다고 생각했는데, 아마 iter되면서 heap안의 값들이 모두 answer에 추가 될것이라고
# 생각했나보다. 사실은 한번밖에 heappop이 없으니 값이 하나밖에 추가되는게 당연

import heapq
from _collections import deque as queue

# health 오름차순 정렬
# 인덱스를 리턴해야 하므로, (공격치, 낮추는 체력, 인덱스)를 튜플로 하여 낮추는 체력 기준으로 정렬

def solution(healths, items):
    healths.sort()
    new_items = queue(sorted([(h, a, idx) for idx, (a, h) in enumerate(items)]))
    heap = []
    answer = []
    print(healths)
    print(new_items)
    for health in healths:
        while new_items:
            h, a, idx = new_items[0]
            if health - h < 100:
                break
            h, a, idx = new_items.popleft()
            heapq.heappush(heap, (-a, idx + 1))
        if heap:
            answer.append(heapq.heappop(heap)[1])
    return sorted(answer)
