def solution(m, n, puddles):
    answer = 0
    # matrix 생성 (with puddles)
    matrix = [[1 for c in range(m)] for _ in range(n)]
    matrix[0][0], matrix[n - 1][m - 1] = 1, 1
    for y, x in puddles:
        matrix[y - 1][x - 1] = 0
    # 1에서 1까지 가는 방법을 계속 만들어낸다
    # 도중에 -1 이 있으면 그 방법은 폐기
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for r in range(n):
        for c in range(m):
            for i in range(4):
                nx = c + dx[i]
                ny = r + dy[i]
                if (0 < nx < m) and (0 < ny < n) and (matrix[ny][nx] != 0):
                    matrix[ny][nx] = matrix[ny - 1][nx] + matrix[ny][nx - 1]
    # print(matrix)
    # for m in matrix:
    #     print(m)

    return matrix[n - 1][m - 1]


m = 4
n = 3
puddles = [[2, 2]]

print(solution(m, n, puddles))
