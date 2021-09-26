from collections import deque


def solution(n, computers):
    visited = [0] * n
    visited[0] = 1
    queue = deque()
    queue.append(0)
    answer = 0
    while queue:
        pops = queue.popleft()
        for idx, value in enumerate(computers[pops]):
            if value == 1 and visited[idx] == 0:
                visited[idx] = 1
                queue.append(idx)
        if not queue and 0 in visited:
            answer += 1
            idx = visited.index(0)
            queue.append(idx)
    return answer + 1


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	#[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
