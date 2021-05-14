from collections import deque


def solution(n, signs):
    for start in range(n):
        queue = deque([end for end, sign in enumerate(signs[start]) if sign])

        while queue:  # 중간 경로가 있다면
            route = queue.popleft()  # 그 중간경로를 목적지와 이었을 때 1인지 검사
            for end, sign in enumerate(signs[route]):  # sign 이 결국 1이면 이어져 있다는 말
                if not signs[start][end] and sign:
                    queue.append(end)  # 왜 넣어주냐 => end가 또 하나의 중간경로가 되기에
                    signs[start][end] = 1
    return signs


signs = [[0, 0, 1], [0, 0, 1], [0, 1, 0]]
n = len(signs)
