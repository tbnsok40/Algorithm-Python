import copy

def removeSame(m, n, matrix, ):
    remove = []
    before_matrix = copy.deepcopy(matrix)

    for r in range(m):
        for c in range(n):
            c_ = c + 1
            r_ = r + 1
            if c_ < n and r_ < m:
                if matrix[r][c] == matrix[r_][c] == matrix[r][c_] == matrix[r_][c_]:
                    # 복사본 같은걸 만들어서, 조건 만족하는 모든 부분 0으로 만든다음에, 전체 순회.
                    remove.append((r, c))
    for rem in remove:
        r_, c_ = rem[0], rem[1]
        matrix[r_][c_], matrix[r_][c_ + 1], matrix[r_ + 1][c_], matrix[r_ + 1][c_ + 1] = 0, 0, 0, 0
    if before_matrix == matrix:

        return True
    else:
        return False


def solution(m, n, board):
    matrix = []
    for row in board:
        matrix.append(list(row))
    while True:
        a = removeSame(m, n, matrix)
        print(a)
        break
        # 한번 삭제되면 이동/ 조정 함수가 필요
    # for m in matrix:
    #     print(m)
    print(matrix)
    answer = 0
    return answer


# 2 x 2 면 지워지는 함수


m = 4  # row
n = 5  # column
board = ["CCBDE",
         "AAADE",
         "AAABF",
         "CCBBF"]

print(solution(m, n, board))
