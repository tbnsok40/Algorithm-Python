def solution(rows, columns, queries):

    matrix = [[i + (j * columns) for i in range(1, columns + 1)] for j in range(rows)]

    for x1, y1, x2, y2 in queries:

        left = x1 - 1
        top = y1 - 1
        right = x2 - 1
        bottom = y2 - 1

        temp = matrix[top][left]

        for k in range(top, bottom):
            value = matrix[k + 1][left]
            matrix[k][left] = value

        for i in range(left, right):
            value = matrix[bottom][i + 1]
            matrix[bottom][i] = value

        for p in range(bottom, top, -1):
            value = matrix[p - 1][right]
            matrix[p][right] = value

        for j in range(right, left, -1):
            value = matrix[top][j - 1]
            matrix[top][j] = value

        # matrix[top][left] = temp

        for j in matrix:
            print(j)
        break
        # for i in range():


    return


rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

print(solution(rows, columns, queries))
