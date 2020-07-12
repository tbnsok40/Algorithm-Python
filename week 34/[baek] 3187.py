import sys
from collections import deque

input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    v_cnt = 0
    k_cnt = 0
    visited[x][y] =1 # 까먹지마라
    q.append([x,y])
    while q:
        x,y = q.popleft()
        if a[x][y] == 'v':
            v_cnt += 1
        elif a[x][y] =='k':
            k_cnt += 1
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if (0<= new_x < n) and (0<= new_y<m): # 여기 new_x의 범위가 왜 m(세로길이)와 비교돼야 하는지, new_y도 마찬가지
                if a[new_x][new_y] != '#' and (visited[new_x][new_y]==0):
                    visited[new_x][new_y] =1
                    q.append([new_x,new_y])
    if v_cnt>=k_cnt:
        k_cnt=0
    else:
        v_cnt =0
    return [v_cnt,k_cnt]

m, n = map(int, input().split())
a = [list(input().strip()) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
q = deque()

v, k = 0,0
for i in range(m):
    for j in range(n):
        if a[i][j] != '#' and (visited[i][j]==0):
            v_cnt, k_cnt = bfs(i,j)
            v += v_cnt; k+=k_cnt
print(k,v)
