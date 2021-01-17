import math
from collections import deque

def bfs(start, maps, distance, K):
    queue = deque()
    queue.append(start)

    # 처음 출발한 도시의 distance는 0
    distance[start] = 0

    while queue:
        y = queue.popleft() # y는 출발지가 된다
        for x in range(1, len(maps)):
            if maps[y][x] != 0: # 도로가 있는 경우 (y -> x)
                # 현재까지의 거리 + 이동할 때의 거리가 K보다 작다 (문제 조건)
                # and 이전의 조건은, 목적지(x)까지의 거리를 더 작은 값으로 업데이트하기 위함 (문제 조건)
                if distance[x] > distance[y] + maps[y][x] and K >= distance[y] + maps[y][x]:
                    # distance[x]는 1에서부터 목적지 까지의 거리
                    distance[x] = distance[y] + maps[y][x]
                    queue.append(x) #목적지인 x를 queue에 넣어, pop하면 출발지 y로 바뀐다(line 12)

    return len([i for i in distance if i <= K])


def solution(N, road, K):
    # 시작지점 1에서부터 해당 마을까지의 거리.
    # 초기값을 inf로 설정하고, 계산한 거리가 distance[마을]보다 작으면 distance를 업데이트해준다.
    distance = [math.inf for _ in range(N + 1)]
    # (N+1) x (N+1) 배열 maps 생성
    maps = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for frm, to, w in road:
        # 0이면 초기화한 값 그대로이므로 w값을 넣어준다
        if maps[frm][to] == 0 and maps[to][frm] == 0:
            maps[frm][to], maps[to][frm] = w, w
        else: #이미 if조건에 걸렸던 값들이 또 등장하면, 값 대소비교
            if w < maps[frm][to]:
                maps[frm][to], maps[to][frm] = w, w
    return bfs(1, maps, distance, K)

# N = 5
# K = 3
# road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
# print(solution(N, road, K))