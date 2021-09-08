def solution(n, results):
    matrix = [[None for _ in range(n)] for _ in range(n)]

    for win, lose in results:
        matrix[win - 1][lose - 1] = True
        matrix[lose - 1][win - 1] = False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[i][j] == None:
                    continue
                # refactoring => 이거만 쓰면 터진다 (왜냐, 이전에는 True / False 로 값을 명시해줬지만
                # 아래에선 그저 서로의 값이 같을 때 라는 조건을 단다. 이건 서로가 None 일 때도 조건문을 만족할 수 있기 때문에 에러가 발생한다.
                if matrix[i][j] == matrix[j][k]:
                    matrix[i][k] = matrix[i][j]
                    matrix[k][i] = not matrix[i][k]

    answer = 0
    for i in range(n):
        if None in (matrix[i][:i] + matrix[i][i + 1:]):
            continue
        answer += 1

    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

print(solution(n, results))