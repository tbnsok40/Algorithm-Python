def removeSame(m, n, matrix):
    remove = []

    for r in range(m):
        for c in range(n):
            c_ = c + 1
            r_ = r + 1
            if c_ < n and r_ < m:
                if matrix[r][c] == matrix[r_][c] == matrix[r][c_] == matrix[r_][c_] and (matrix[r][c] != "-"):
                    remove.append((r, c))
    if remove:
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
    while True:
        if removeSame(n, m, matrix):
            for t in matrix:
                while 0 in t:
                    count += 1
                    t.remove(0)
                    t.insert(0, "-")
        else:
            break
    return count



m = 4  # row
n = 5  # column
board = ["CCBDE",
         "AAADE",
         "AAABF",
         "CCBBF"]
#
# m = 6  # row
# n = 6  # colum
# board = ["TTTANT",
#          "RRFACC",
#          "RRRFCC",
#          "TRRRAA",
#          "TTMMMF",
#          "TMMTTJ"]

print(solution(m, n, board))
