def solution(N, mine):
    matrix = [[0] * (N + 2) for _ in range(N + 2)]

    for a, b in mine:
        matrix[a][b] = -1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if matrix[i][j] == -1:
                around(i, j, matrix)

    result = []
    for i in range(1, N + 1):
        result.append(matrix[i][1: N + 1])

    # for m in result:
    #     print(m)

    return result


def around(i, j, matrix):
    around_index = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),

        (i, j - 1),
        (i, j + 1),

        (i + 1, j + 1),
        (i + 1, j),
        (i + 1, j - 1),
    ]

    for a, b in around_index:
        if matrix[a][b] != -1:
            matrix[a][b] += 1
    return


mine = [
    [1, 1],
    [1, 7],
    [2, 7],
    [3, 6],
    [4, 1],
    [4, 4],
    [4, 8],
    [8, 4],
    [8, 5],
    [9, 6]
]
N = 9
print(solution(N, mine))
