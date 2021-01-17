from collections import deque

def valid(x, y, n, m):
    return 0 <= x < m and 0 <= y < n

def solution(m, n, infests, vaccinateds):
    answer = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    visited = [[False] * n for _ in range(m)]
    num_emp = m * n  # 빈칸 수

    for vaccinated in vaccinateds:
        a, b = vaccinated
        visited[a - 1][b - 1] = True
        num_emp -= 1

    for infest in infests:
        a, b = infest
        visited[a - 1][b - 1] = True
        num_emp -= 1
        q.append([a - 1, b - 1, 0])

    while num_emp > 0 and len(q) > 0:
        cur_x, cur_y, cur_day = q.popleft()
        for d in range(4):
            next_x = cur_x + dx[d]
            next_y = cur_y + dy[d]
            if not valid(next_x, next_y, n, m) or visited[next_x][next_y]:
                continue
            visited[next_x][next_y] = True
            num_emp -= 1
            q.append([next_x, next_y, cur_day + 1])
            answer = cur_day + 1

    return answer if num_emp <= 0 else -1

m = 2
n = 4
infests = [[1,4],[2,2]]
vaccinateds = [[1,2]]

# m = 2
# n = 3
# infests = [[2,2]]
# vaccinateds = [[1,2],[2,1],[2,3]]

print(solution(m,n,infests,vaccinateds))