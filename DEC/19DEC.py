board = [[0, 0, 1, 1], [1, 1, 1, 1]]
board = [[0,1,1,1],[1,1,1,0],[1,1,1,1],[0,0,1,0]]

import itertools

def solution(board):
    M, N = len(board), len(board[0])
    for i in range(1, M):
        for j in range(1, N):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                for j in board:
                    print(j)
                print(' ')

    return max(itertools.chain(*board))**2
print(solution(board))



my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])
print(answer)

# 방법 2 - itertools.chain
import itertools
print(list(itertools.chain.from_iterable(my_list)))


import itertools
print(list(itertools.chain(*my_list)))
