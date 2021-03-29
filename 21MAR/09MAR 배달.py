# 다익스트라 알고리즘
# 방향이 있는 그래프
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # float('inf') : 양의 무한대를 나타냄 <--> float('-inf')
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    # 굳이 우선순위 큐를 선언하는 이유, 가장 작은 값을 젤 먼저 빼내기 위함

    while queue:
        print(queue)

        current_distance, current_destination = heapq.heappop(queue) # 힙큐로 선언했기에, 가장 짧은 distance를 가진 노드가 먼저 나온다.

        if distances[current_destination] < current_distance: # false가 뜬다면 아래 for문으로 넘어간다 (current_distance가 기존 거리보다 짧아야함)
        # 첫 조건문에서 false가 뜨기에(boolean 양쪽 모두 0) 바로 for문으로 넘어간다.
            continue
        # heapq 덕분에 가장 짧은 거리의 node를 뽑아내서 graph[]에 넣는다.
        for new_destination, new_distance in graph[current_destination].items(): # .items() : 튜플로 만든다.
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination]) # 거리값과 노드를 배열형태로 묶어 다시 우선순위 큐에 삽입

    return distances
print(dijkstra(graph, 'A'))