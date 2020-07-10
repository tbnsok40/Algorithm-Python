from collections import deque
import sys

input = sys.stdin.readline()
dx = [1,-1,0,0]
dy = [0,0,1,-1]

m, n = map(int, input().split())
a = [list(input().split() for _ in range(m))]
visited = [[0]*n for _ in range(m)]
q = deque()

v, k = 0,0
for i in range(m):
    for j in range(n):
        if (a[i][j] != '#') and (visited[i][j] == 0):
            v_cnt, k_cnt = bfs(i,j)
            v += v_cnt
            k += k_cnt
print(k,v)

def bfs(x,y):
    q.append([x,y])
    v_cnt, k_cnt = 0,0
    while q:
        x,y = q.popleft()
        if a[x][y] == 'v':
            v_cnt += 1
        elif a[x][y] == 'k':
            k_cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < m and 0 <= ny < n:
                visited[nx][ny] = 1 # visited
                q.append([nx,ny]) # 이런 구조의 bfs는, 이미 지났던 점에 대해서 또 추가 되는 경우는 있을 수 없나?
    if v_cnt >= k_cnt:
        k_cnt =0
    else:
        v_cnt = 0
    return [v_cnt,k_cnt]


