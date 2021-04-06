def solution(n, computers):
    visited = [0] * n
    result = 0
    bfs = list()

    while 0 in visited:
        bfs.append(visited.index(0))
        while bfs:
            curr = bfs.pop()
            visited[curr] = 1
            print(visited)
            for i in range(n):
                if computers[curr][i] == 1 and visited[i] == 0:
                    bfs.append(i)
        result += 1

    return result


# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3

# n 이 필요한가?


print(solution(n, computers))
