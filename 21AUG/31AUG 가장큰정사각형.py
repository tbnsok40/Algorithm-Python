def solution(board):
    row = len(board)
    column = len(board[0])
    answer = 1
    temp = 0
    for r in range(row):
        for c in range(column):
            temp += board[r][c]
            if (r + 1 <= row - 1) and (c + 1 <= column - 1):
                if board[r][c] and board[r + 1][c] and board[r][c + 1] and board[r + 1][c + 1]:
                    board[r + 1][c + 1] = min(board[r][c], board[r + 1][c], board[r][c + 1]) + 1
                    answer = max(answer, board[r + 1][c + 1])
    if not temp:
        return 0
    return answer ** 2


board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
print(solution(board))
