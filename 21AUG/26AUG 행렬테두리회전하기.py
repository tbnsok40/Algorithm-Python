def solution(rows, columns, queries):
    answer = []
    matrix = [[i + (j * columns) for i in range(1, columns + 1)] for j in range(rows)]

    for y1, x1, y2, x2 in queries:

        top = y1 - 1
        left = x1 - 1
        bottom = y2 - 1
        right = x2 - 1

        temp = matrix[top][left]
        minimum = temp

        for k in range(top, bottom):
            value = matrix[k + 1][left]
            matrix[k][left] = value
            minimum = min(minimum, value)

        for i in range(left, right):
            value = matrix[bottom][i + 1]
            matrix[bottom][i] = value
            minimum = min(minimum, value)

        for p in range(bottom, top, -1):
            value = matrix[p - 1][right]
            matrix[p][right] = value
            minimum = min(minimum, value)

        for j in range(right, left, -1):
            value = matrix[top][j - 1]
            matrix[top][j] = value
            minimum = min(minimum, value)

        matrix[top][left + 1] = temp
        answer.append(minimum)

    return answer


rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

print(solution(rows, columns, queries))
