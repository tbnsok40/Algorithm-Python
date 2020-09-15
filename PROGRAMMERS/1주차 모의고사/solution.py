m, n = 2, 4
infests = [[1,4],[2,2]]
vaccinateds = [[1,2]]

# m, n = 2, 2
# infests = [[1, 1], [2, 2]]
# vaccinateds = 	[[1, 2], [2, 1]]
#
m, n = 2, 3
infests = [[2, 2]]
vaccinateds = 	[[1, 2], [2, 1], [2, 3]]
#
# m, n = 3, 4
# infests = [[1,2],[1,4]]
# vaccinateds = 	[[1,3],[2,3],[3,3]]
from collections import deque
def solution(m, n, infests, vaccinateds):
    queue = deque()
    field = [[0 for _ in range(n+1)] for _ in  range(m+1)]

    for (i, j) in vaccinateds:
        field[i][j] = 'v'
    for (i, j) in infests:
        queue.append((i,j))
        field[i][j] = 'i'

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# for infests
    day = 0
    temp = deque()

    while queue:
        i, j = queue.popleft()
        for dx, dy in dirs:
            ny = i + dy
            nx = j + dx

            if (0 < nx <= n) and (0 < ny <= m) and (field[ny][nx] == 0) and (field[ny][nx] != 'i'):
                field[ny][nx] = 'i'
                temp.append((ny, nx))

        if len(queue) == 0:
            queue = temp
            temp = deque()
            day += 1
    print(field)
    #################### 이부분이 필요했네
    for i in range(m):
        field[i][0] = 1
    for i in range(1,n+1):
        if 0 in field[i]:
            return -1
    ######################
    return day-1

print(solution(m, n, infests, vaccinateds))

#-1 이 나와야 하는 코드를 못짜겠다..