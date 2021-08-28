# def solution(rows, columns, queries):
#     answer = []
#
#     # i, j 보다는 column, row 를 사용하여 명시해주자.
#     # matrix = [[i + (j * columns) for i in range(1, columns + 1)] for j in range(rows)]
#     matrix = [[(row * columns) + (col + 1) for col in range(columns)] for row in range(rows)]
#
#     # queries 원소의 위치를 잘 파악하자. 인덱스0부터 시작하므로 1씩 빼주는 작업 필요
#     for top, left, bottom, right in queries:
#         top = top - 1
#         left = left - 1
#         bottom = bottom - 1
#         right = right - 1
#
#         temp = matrix[top][left]
#         minimum = temp
#
#         for k in range(top, bottom):  # top => bottom 방향이므로, 역으로 아래에 있는걸 위에 대입해준다.
#             value = matrix[k + 1][left]
#             matrix[k][left] = value
#             minimum = min(minimum, value)
#
#         for i in range(left, right):
#             value = matrix[bottom][i + 1]
#             matrix[bottom][i] = value
#             minimum = min(minimum, value)
#
#         for p in range(bottom, top, -1): # 굳이 -1 을 쓰는 이유는 값이 겹치지 않게 하기 위함.
#             value = matrix[p - 1][right] # 위에서 아래로 방향이므로, 맨 아래서부터, 위에 있는 걸 아래에 대입해준다.
#             matrix[p][right] = value
#             minimum = min(minimum, value)
#
#         for j in range(right, left, -1):
#             value = matrix[top][j - 1]
#             matrix[top][j] = value
#             minimum = min(minimum, value)
#
#         matrix[top][left + 1] = temp
#         answer.append(minimum)
#
#     return answer
#


def solution(rows, columns, queries):
    matrix = [[(row * columns) + (col + 1) for col in range(columns)] for row in range(rows)]
    answer = []
    for top, left, bottom, right in queries:
        top, left, bottom, right = top - 1, left - 1, bottom - 1, right - 1

        temp = matrix[top][left]
        minimum = temp

        for i in range(top, bottom):
            value = matrix[i + 1][left]
            matrix[i][left] = value
            # print(value) range 에 의해 3칸만 출력됨 -> 한자리는 빈다는 말.
            minimum = min(minimum, value)

        for i in range(left, right):
            value = matrix[bottom][i + 1]
            matrix[bottom][i] = value
            minimum = min(minimum, value)

        for i in range(bottom, top, -1):
            value = matrix[i - 1][right]
            matrix[i][right] = value
            minimum = min(value, minimum)

        for i in range(right, left, -1):
            value = matrix[top][i - 1]
            matrix[top][i] = value
            minimum = min(value, minimum)

        answer.append(minimum)
        matrix[top][left + 1] = temp

    return answer


rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

print(solution(rows, columns, queries))
