def dfs(board, base_row, base_col, count, stack):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = dx[i] + base_col
        ny = dy[i] + base_row
        if (0 <= ny <= 5) and (0 <= nx <= 5) and board[base_row][base_col] == board[ny][nx]:
            count += 1
            stack.append([ny, nx])
            dfs(board, ny, nx, count, stack)
        else:
            if count >= 3:
                print(stack)
            else:
                continue
    return count

    # count 3 이상이면 삭제한다. 그럼 count +1 할 때의 ny, nx 도 queue에 담는다.


def solution(macaron):
    board = [[0] * 6 for _ in range(6)]

    for column, color in macaron:
        base_col = column - 1

        for row in range(5, -1, -1):
            if board[row][column - 1] == 0:
                board[row][column - 1] = color
                base_row = row
                break

        # 마카롱 하나가 떨어진 후, 주위녀석들 탐색.
        dfs(board, base_row, base_col, 0, [base_row, base_col])
    # for b in board:
    #     print(b)
    answer = []
    return answer


macaron = [[1, 1], [2, 1], [1, 2], [3, 3], [6, 4], [3, 1], [3, 3], [3, 3], [3, 4], [2, 1]]
print(solution(macaron))
