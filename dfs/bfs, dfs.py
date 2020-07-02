graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


############### DFS #####################
def dfs(graph, start_node):
    visited, need_visit = list(), list()  # 방문한 리스트와 방문해야 할 리스트 생성
    need_visit.append(start_node)  # 시작 노드를 방문해야할 리스트에 삽입

    while need_visit:  # need_visit가 비어있지 않을 때
        node = need_visit.pop()  # 해당 리스트의 마지막 원소 pop // 놀라운 점은 pop(0)으로만 바꿔주면 BFS를 구현할 수 있다.
        if node not in visited:  # visited에 없는 노드이면
            visited.append(node)  # visited에 넣어주고
            need_visit.extend(
                graph[node])  # 해당 노드와 연결된 노드들을 그래프에서 찾아와, 방문해야할 리스트에 넣어준다. 두 줄 위의 조건문에 따라 visited에 이미 있는 노드는 pass
            # 결국 visited에 appending된 순서가 dfs 탐색 순서이다.
    # print(visited)
    return visited


print(dfs(graph, 'A'))
##########################################
# def bfs(graph, start_node):
#     visited, need_visit = list(), list()
#     need_visit.append(start_node)
#
#     while need_visit:
#         node = need_visit.pop(0)
#         if node not in visited:
#             visited.append(node)
#             need_visit.extend(graph[node])
#     print(visited)
#     return 0
# bfs(graph, 'A')


# pop()는 리스트의 마지막 원소를 pop시킨다.
# pop(0)는 큐 처럼 첫 원소 pop
