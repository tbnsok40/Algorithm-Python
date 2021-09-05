def solution(m, n, puddles):
    answer = 0
    # matrix 생성 (with puddles)
    matrix = [[1 for _ in range(m)] for _ in range(n)]
    for y, x in puddles:  # 여길 미리 0으로 해놨으면 안됐나보다. 왜냐면 미리 0이면,,, 안돼나?
        matrix[y - 1][x - 1] = 0
    # 1에서 1까지 가는 방법을 계속 만들어낸다
    # 도중에 -1 이 있으면 그 방법은 폐기
    for r in range(n):
        for c in range(m):
            if [r, c] == [0, 0]:
                continue
            if (0 < c < m) and (0 < r < n) and (matrix[r][c] != 0):
                matrix[r][c] = (matrix[r - 1][c] + matrix[r][c - 1]) % 1000000007

    for k in matrix:
        print(k)

    return matrix[n - 1][m - 1]


m = 4
n = 3
puddles = [[2, 2]]

print(solution(m, n, puddles))
