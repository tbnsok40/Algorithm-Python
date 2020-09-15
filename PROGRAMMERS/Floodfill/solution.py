# from _collections import deque
# def bfs(start, image, visited):
#     queue = deque()
#     queue.append(start)
#     color = image[start[0]][start[1]]
#     dirs = [(0,1),(0,-1),(1,0),(-1,0)]
#
#     while queue:
#         y, x = queue.popleft()
#         visited[y][x] = 1
#         for dy, dx in dirs:
#             ny, nx = y + dy, x + dx
#             if (0 <= ny < len(image)) and (0 <= nx < len(image[0])) and (not visited[ny][nx]) and (image[ny][nx] == color):
#                 visited[ny][nx] = 1
#                 queue.append((ny,nx))
#         return True
#
# def solution(n,m,image):
#     visited = [[0 for _ in range(m)] for _ in range(n)]
#     count = 0
#     for y in range(n):
#         for x in range(m):
#             if not visited[y][x]:
#                 count += bfs((y,x), image, visited)
#     return count

# 아직 탐색하지 않은 공간 => visitied = [[0][0]]으로 초기화
# 파이썬에서 재귀는 느리다고 하니 bfs할 땐 queue로 구성할 것
n = 2
m = 3
image = [[1, 2, 3], [3, 2, 1]]
def solution(n, m, image):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                count += bfs(i, j, image, visited)
    return count

from collections import deque
def bfs(i, j, image, visited):
    queue = deque()
    queue.append((i, j))
    color = image[i][j]
    dirs = [(0, 1), (0, -1),(1,0), (-1,0)]
    # 올바른 인덱스 범위 내에서, color와 같은 값을 가지는 visited..?
    while queue:
        i, j = queue.popleft()
        visited[i][j] = 1

        for dy, dx in dirs:
            nx, ny = j + dx, i + dy
            if (0 <= nx < m) and (0 <= ny < n) and (not visited[ny][nx]) and (color == image[ny][nx]):
                queue.append((ny,nx))
                visited[ny][nx] = 1
        return True
print(solution(n, m, image))