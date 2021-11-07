from itertools import chain


def checkNum(num: int):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


def solution(rows, columns):
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    visited = [[0 for _ in range(columns)] for _ in range(rows)]

    row, col = 0, 0
    recent_num = 1
    flag = "odd"

    board[0][0] = recent_num
    visited[0][0] = flag

    while True:
        for v in chain(*visited):
            if v == 0:
                break
        else:
            break

        if flag == "odd":  # False: 홀수
            col += 1
            if col == columns:
                col = 0
        else:
            row += 1
            if row == rows:
                row = 0
        recent_num += 1
        flag = checkNum(recent_num)

        if visited[row][col] != flag:
            board[row][col] = recent_num
            visited[row][col] = flag
        else:
            break

    return board


rows = 3
columns = 3
print(solution(rows, columns))
# [[8,2,13,14],[16,10,4,15],[17,11,12,6]]
