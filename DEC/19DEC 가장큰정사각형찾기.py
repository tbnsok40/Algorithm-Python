board = [[0, 0, 1, 1], [1, 1, 1, 1]]
board = [[0,1,1,1],[1,1,1,0],[1,1,1,1],[0,0,1,0]]

import itertools

def solution(board):
    M, N = len(board), len(board[0])
    for i in range(1, M):
        for j in range(1, N):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
    return max(itertools.chain(*board))**2
print(solution(board))