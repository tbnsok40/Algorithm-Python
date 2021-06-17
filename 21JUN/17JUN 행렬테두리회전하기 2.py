def solution(rows, columns, queries):

    matrix = [[i + (j * columns) for i in range(1, columns + 1)] for j in range(rows)]

    for x1, y1, x2, y2 in queries:

        left = x1
        top = y1
        right = x2
        bottom = y2

        for i in range(right, left, -1):
            # print(i)
            matrix[top][i - 1] = matrix[top][i]
        print(matrix)





    return


rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

print(solution(rows, columns, queries))
