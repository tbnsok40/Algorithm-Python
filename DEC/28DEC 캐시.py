deque에서도 remove는 된다.

from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0 :
        return len(cities) * 5

    new_cities = deque([i.lower() for i in cities])
    # queue = deque()
    # for _ in range(cacheSize):
    #     count += 5
    #     queue.append(new_cities.popleft())
    queue = deque([new_cities.popleft()])
    count = 5
    while new_cities:
        pops = new_cities.popleft()
        if pops in queue and cacheSize > len(queue):
            count += 1
            queue.remove(pops)
        elif cacheSize > len(queue):
            count += 5
        elif pops in queue:
            count += 1
            queue.remove(pops)

        else:
            count += 5
            queue.popleft() # indexError가 일어나기 전에 append됐어야 했는데 왜...?

        queue.append(pops)
    return count