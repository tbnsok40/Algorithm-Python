# deque에서도 remove는 된다.
# cities 배열 -> 1. 모두 소문자화, 2. 리스트 deque 변형
#  deque을 popleft
# cache_queue(deque)에 append, popleft

from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    new_cities = deque([i.lower() for i in cities])
    # queue = deque()
    # for _ in range(cacheSize):
    #     count += 5
    #     queue.append(new_cities.popleft()) <- 이걸 하면 안되는게, 초기 캐시 채우기 전에, cache hit이 발생하는 경우를 고려 하지 않았기 때문
    queue = deque([new_cities.popleft()])
    count = 5
    while new_cities:
        pops = new_cities.popleft()
        if pops in queue and cacheSize > len(queue): # 이 조건이 다른 조건보다 먼저 있어야, 초기 cache size를 채우기 이전에 cache hit이 발생하는 경우를 고려할 수 있다.
            count += 1
            queue.remove(pops)

        elif pops in queue:
            count += 1
            queue.remove(pops)
        elif cacheSize > len(queue):
            count += 5
        else:
            count += 5
            queue.popleft()  # indexError가 일어나기 전에 append됐어야 했는데 왜...?

        queue.append(pops)
    return count

cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA',
          'SanFrancisco', 'Seoul', 'Rome', 'Paris',
          'Jeju', 'NewYork', 'Rome']

cacheSize = 5

print(solution(cacheSize, cities))
