def solution(triangle):

    for i in range(1, len(triangle)):
        col_length = len(triangle[i])
        for j in range(col_length):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == col_length - 1:  # 여기서 -1 해주지 않으면 index 초
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    return max(triangle[-1])


# def solution(triangle):
#     triangle = [[0] + t + [0] for t in triangle]
#     for i in range(1, len(triangle)):
#         for j in range(1, i + 2):
#             triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
#     return max(triangle[-1])
# 예외처리 연산이 편하게 허깨비를 세운다. (indexError 안나도록)

print(solution(triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
