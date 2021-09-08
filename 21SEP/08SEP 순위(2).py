def solution(n, results):
    matrix = [[None for _ in range(n)] for _ in range(n)]

    for win, lose in results:
        matrix[win - 1][lose - 1] = True
        matrix[lose - 1][win - 1] = False

    for i in range(n):
        for j in range(n):
            for k in range(n):

                # if (matrix[i][j] == False) and (matrix[j][k] == False):
                #     matrix[i][k] = False
                #     matrix[k][i] = True
                # if (matrix[i][j] == True) and (matrix[j][k] == True):
                #     matrix[i][k] = True
                #     matrix[k][i] = False

                # refactoring
                if matrix[i][j] == matrix[j][k]:
                    matrix[i][k] = matrix[i][j]
                    matrix[k][i] = not matrix[i][k]




    # for m in matrix:
    #     print(m)

    answer = 0
    for i in range(n):
        if None in (matrix[i][:i] + matrix[i][i + 1:]):
            continue
        answer += 1

    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

print(solution(n, results))