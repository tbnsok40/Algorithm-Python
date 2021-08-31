from collections import deque


def solution(n, m, images):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    answer = 0

    for r in range(n):
        for c in range(m):
            if images[r][c] == -1:
                continue
            color = images[r][c]
            queue = deque([(r, c)])
            while queue:
                y, x = queue.popleft()
                for ny, nx in directions:
                    py = ny + y
                    px = nx + x
                    if (0 <= py < n) and (0 <= px < m) and (images[py][px] == color):
                        images[py][px] = -1
                        queue.append((py, px))
            answer += 1
    return answer


n = 2
m = 3
images = [[1, 2, 3], [3, 2, 1]]
print(solution(n, m, images))

# bfs, queue에 들어가는 것이 무슨 의미인지 파악하기
