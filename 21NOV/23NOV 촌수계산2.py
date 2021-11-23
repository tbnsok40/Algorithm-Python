from collections import deque


def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        for no in graph[node]:
            if checked[no] == 0:
                checked[no] = checked[node] + 1
                queue.append(no)


n = int(input())
graph = [[] for _ in range(n + 1)]
s, e = map(int, input().split())
checked = [0] * (n + 1)

for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


bfs(s)
print(checked[e] if checked[e] > 0 else -1)

# 함수에서 none 이 출력되면 안된다.


"""
9
8 2
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
"""
