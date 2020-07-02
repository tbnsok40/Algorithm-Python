import sys
from collections import deque


def dfs(graph, start):
    visited, need_visit = list(), list()
    need_visit.append(start)
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                temp = list(set(graph[node]) - set(visited))
                temp.sort(reverse=True)
                need_visit += temp
    # need_visit.extend(graph[node]) <== 이게 런타임 에러를 일으킨다(그리고 필요없는 부분임)
    return visited


def bfs(graph, start):
    visited, need_visit = list(), list()
    need_visit = deque([start])
    # need_visit.append(start)
    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            if node in graph:
                temp = list(set(graph[node]) - set(visited))
                temp.sort()
                need_visit += temp
    return visited


graph = dict()
n = sys.stdin.readline().split(' ')
node, edge, start = [int(i) for i in n]

for i in range(edge):
    node1, node2 = map(int, sys.stdin.readline().split())
    if node1 not in graph:
        graph[node1] = [node2]
    elif node2 not in graph[node1]:
        graph[node1].append(node2)

    if node2 not in graph:
        graph[node2] = [node1]
    elif node1 not in graph[node2]:
        graph[node2].append(node1)

print(*dfs(graph, start))
print(*bfs(graph, start))
