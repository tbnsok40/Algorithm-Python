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
<<<<<<< HEAD
    # index 일 뿐 값이 아니다. (top 보다 bottom이 크고, left보다 right가 크다)
    answer = []

=======

    # index 일 뿐 값이 아니다.
>>>>>>> c893f83f45c31304cf43f05ced6a422454509a18
    for x1, y1, x2, y2 in queries:
        top = x1 - 1
        left = y1 - 1
        bottom = x2 - 1
        right = y2 - 1

        temp = matrix[top][left]
<<<<<<< HEAD
        mini = temp

        for i in range(bottom, top, -1):  # top < bottom # desc
            value = matrix[i - 1][right]
            matrix[i][right] = value
            mini = min(mini, value)

        for i in range(left, right):
            value = matrix[bottom][i + 1]
            matrix[bottom][i] = value
            mini = min(mini, value)

        for i in range(top, bottom):  # top < bottom
            value = matrix[i + 1][left]
            matrix[i][left] = value
            mini = min(mini, value)

        # 얘가 무조건 마지막에 있어야한다. but why?
        for i in range(right, left, -1):
            value = matrix[top][i - 1]
            matrix[top][i] = value
            mini = min(mini, value)

        matrix[top][left + 1] = temp
        answer.append(mini)

        for i in matrix:
            print(i)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
=======

        for i in range(left, right):
            matrix[top][i] = matrix[top][i + 1]

        for i in range(right, bottom):
            matrix[i][right] = matrix[i + 1][right]
    print(matrix)







    answer = []
    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
>>>>>>> c893f83f45c31304cf43f05ced6a422454509a18

# rows:
# columns:
# queries:

# 1. rows, columns, 로 매트릭스 만든다.
# 2. queries 를 한칸씩 돌릴 수 있는 로직 만들어야한다.
# 3.

