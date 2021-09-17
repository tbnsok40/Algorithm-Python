# floyd-warshall 이 실패했던 이유
# 1. 플로이드 워셜을 잘못 이해한점
# 2. 시간초과 날 것을 생각 못한
# def solution(n, edge):
#     # 우선 반쪽짜리 매트릭스를 만들고,
#     matrix = [[0] * n for _ in range(n)]
#     graph = {}
#
#
#     for a, b in edge:
#         matrix[a - 1][b - 1] = 1
#         matrix[b - 1][a - 1] = 1
#
#         graph[a] = graph.get(a, []) + [b] # defaultdict(list), append 하는 것과 같은 방식 .
#         print(graph[a])
#     for m in matrix:
#         print(m)
#     # print(' ')
#     for i in range(1, n):
#         if matrix[0][i] == 0:
#             maximum = float('inf')
#             temp = []
#             for j in range(1, i):
#                 if i == 5:
#                     print('j', j, 'matrix[0][j]: ', matrix[0][j], ' matrix[j][i]', matrix[j][i])
#                 # maximum = min(maximum, matrix[0][j] + matrix[j][i])
#                 temp.append(matrix[0][j] + matrix[j][i])
#             print(i, min(temp), matrix[0][i])
#             matrix[0][i] = min(temp)
#             # matrix[0][i] = maximum
#     for m in matrix:
#         print(m)
#     # print(' ')
#
#     return matrix[0].count(max(matrix[0]))

from collections import deque
def solution(n, edge):
    # graph = dict()
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        # graph[a] = graph.get(a, []) + [b]
        # graph[b] = graph.get(b, []) + [a]

    visited = [0] * (n + 1)
    queue = deque()
    queue.append(1)
    visited[1] = 1 # 1은 이미 방문한 것으로 설정 (if 조건에서 0 일 때 un-visited 이므로)

    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if visited[node] == 0:
                queue.append(node)
                print('now: ', now, 'node: ',node, 'visited[now] + 1: ', visited[now] + 1)
                visited[node] = visited[now] + 1
    print(visited)
    maximum = max(visited)
    return visited.count(maximum)


n = 6
# edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
edge = [[1, 2], [2, 4], [2, 3], [1, 4], [2, 5], [3, 6], [4, 5], [5, 6]]
print(solution(n, edge))
