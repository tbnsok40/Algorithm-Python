def find_cross(l, r):
    global cross

    a, b, e = l
    c, d, f = r
    try:
        x = (b * f - e * d) / (a * d - b * c)
        y = (e * c - a * f) / (a * d - b * c)

        if (x == int(x)) and (y == int(y)) and [int(x), int(y)] not in cross:
            cross.append([int(x), int(y)])

    except ZeroDivisionError:
        pass


def solution(line):
    global cross
    cross = []

    for l in line:
        for r in line:
            if l != r:
                find_cross(l, r)

    # ready for cross spot
    max_x = -1
    max_y = -1
    min_x = float('inf')
    min_y = float('inf')

    for a, b in cross:
        if a > max_x:
            max_x = a
        if a < min_x:
            min_x = a
        if b > max_y:
            max_y = b
        if b < min_y:
            min_y = b

    row = abs(max_y - min_y) + 1
    col = abs(max_x - min_x) + 1

    board = [["."] * col for _ in range(row)]

    for x, y in cross:
        board[x - min_x][max_y + y] = '*'
    board = list(map(list, zip(*board)))
    result = []
    for b in board[::-1]:
        result.append(''.join(b))
    return result

# result = []
# for i in range(len(board[0]) - 1, -1, -1):
#     temp = []
#     for j in range(len(board)):
#         temp.append(board[j][i])
#     result.append(temp)
# answer = []
# for r in result:
#     answer.append(''.join(r))
# return answer


print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))


print(400/7)