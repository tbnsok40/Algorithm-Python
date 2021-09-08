def solution(n, results):
    matrix = [[None for _ in range(n)] for _ in range(n)]

    for win, lose in results:
        matrix[win - 1][lose - 1] = True
        matrix[lose - 1][win - 1] = False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (matrix[i][j] == False) and (matrix[j][k] == False):
                    matrix[i][k] = False
                    matrix[k][i] = True
                if (matrix[i][j] == True) and (matrix[j][k] == True):
                    matrix[i][k] = True
                    matrix[k][i] = False

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

"""
n 개의 노드
하나의 노드 , n - 1 개의 노드 
1) 연결된 경우가 n - 1 이면, 순위가 결정 된 것
2) 연쇄적으로 순위를 확인하는 방법 : a가 b 에게 지고, b 가 c에게 졌으면, a 는 c 에게 진 것. ㅋㅋㅋㅋ 수 적으면 4중 for문도 해도 됐겠네

조건의 크기가 작으므로 플로이드 워셜( O(n^3) )로 가도 된다.
"""
