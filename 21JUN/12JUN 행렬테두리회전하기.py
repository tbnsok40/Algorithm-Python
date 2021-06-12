def make_matrix(rows, columns):
    start = 1
    mid = 1 + columns
    matrix = []

    for r in range(1, rows + 1):
        row = [c for c in range(start, mid)]
        matrix.append(row)
        start = mid
        mid = columns * (r + 1) + 1

    return matrix


def solution(rows, columns, queries):

    matrix = make_matrix(rows, columns)

    # index 일 뿐 값이 아니다.
    for x1, y1, x2, y2 in queries:
        top = x1 - 1
        left = y1 - 1
        bottom = x2 - 1
        right = y2 - 1

        temp = matrix[top][left]

        for i in range(left, right):
            matrix[top][i] = matrix[top][i + 1]

        for i in range(right, bottom):
            matrix[i][right] = matrix[i + 1][right]
    print(matrix)







    answer = []
    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))

# rows:
# columns:
# queries:

# 1. rows, columns, 로 매트릭스 만든다.
# 2. queries 를 한칸씩 돌릴 수 있는 로직 만들어야한다.
# 3.

