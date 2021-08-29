import copy


def removeSame(m, n, matrix):
    remove = []

    for r in range(m):
        for c in range(n):
            c_ = c + 1
            r_ = r + 1
            if c_ < n and r_ < m:
                if matrix[r][c] == matrix[r_][c] == matrix[r][c_] == matrix[r_][c_] and (matrix[r][c] != "-"):
                    remove.append((r, c))
    print("len(remove)", len(remove))
    if len(remove) > 0:
        for rem in remove:
            r_, c_ = rem[0], rem[1]
            matrix[r_][c_], matrix[r_][c_ + 1], matrix[r_ + 1][c_], matrix[r_ + 1][c_ + 1] = 0, 0, 0, 0
        return True
    else:
        return False


def solution(m, n, board):
    matrix = []
    count = 0
    for row in board:
        matrix.append(list(row))

    matrix = list(map(list, zip(*matrix)))
    i = 0
    while i < 1:
        if removeSame(n, m, matrix):
            for t in matrix:
                while 0 in t:
                    count += 1
                    t.remove(0)
                    t.append("-")
        else:
            pass
        i += 1

    if removeSame(n, m, matrix):
        for t in matrix:
            while 0 in t:
                count += 1
                t.remove(0)
                t.append("-")

    for m in matrix:
        print(m)

    print(count)

    return



# while True:
#     a = removeSame(m, n, matrix)
#     print(matrix)
#     changed = changeRowColumn(matrix, m) # 한번만 전치시키고 계속 밀어내고 지우면 된다. 그리고 삭제된 것만 카운팅하면되구나. 개쩐
#     print(2, changed)
#     if not a:
#         break
# break
# 한번 삭제되면 이동/ 조정 함수가 필요
# for m in matrix:
#     print(m)
# answer = 0

# 2 x 2 면 지워지는 함수


# m = 4  # row
# n = 5  # column
# board = ["CCBDE",
#          "AAADE",
#          "AAABF",
#          "CCBBF"]

m = 6  # row
n = 6  # colum
board = ["TTTANT",
         "RRFACC",
         "RRRFCC",
         "TRRRAA",
         "TTMMMF",
         "TMMTTJ"]

print(solution(m, n, board))
