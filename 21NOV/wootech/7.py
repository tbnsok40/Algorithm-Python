def solution(grid, clockwise):
    board = []
    answer = []
    for g in grid:
        board.append(list(g))
    for i in range(len(board) - 1, -1, -1):
        if i != len(board) - 1:
            N = len(board[i]) // 2
            for c in range(1, N):
                board[i][c : 2 * c + 1]


        else:
            answer.append(i)

        print(i)

    print(board)
    answer = []
    return answer


grid = ["A", "MAN", "DRINK", "WATER11"]
clockwise = "false"

print(solution(grid, clockwise))
