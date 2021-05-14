board = [[0, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [0, 0, 1, 0]]

# board = [[0, 0, 1, 1],
#          [1, 1, 1, 1]]

# def solution(board):
#     for row in board:  # 정답의 최소값이 0인지 1인지 먼저 판별 => 그러니까 싹다 0 인 경우를 거른다.
#         if sum(row):
#             answer = 1
#             break
#     else:
#         return 0
#
#     for i in range(1, len(board)):  # 행
#         for j in range(1, len(board[0])):  # 열
#             if board[i - 1][j - 1] and board[i - 1][j] and board[i][j - 1] and board[i][j]:  # 네칸 모두 1일 때
#                 board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
#                 answer = max(answer, board[i][j])
#     return answer ** 2


# def solution(board):
#     # 잘 설계된 풀이 => for ~ else 구문
#     for row in board:
#         if sum(row):
#             answer = 1
#             break
#     else:
#         return 0
#
#     for i in range(1, len(board)):
#         for j in range(1, len(board[0])):
#             if board[i - 1][j - 1] and board[i - 1][j] and board[i][j - 1] and board[i][j]:
#                 board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
#                 print(i, j, answer, board[i][j])
#                 answer = max(answer, board[i][j])
#     return answer ** 2

# for ~ else 구문은 결국 break 까지 핵심 : for ~ if ~ break ~ else


# def solution(board):
#     for row in board:
#         if sum(row):
#             answer = 1
#             break
#     else:
#         return 0
#
#     for i in range(1, len(board)):
#         for j in range(1, len(board[0])):
#             if board[i - 1][j - 1] and board[i - 1][j] and board[i][j - 1] and board[i][j]:
#                 board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
#                 answer = max(answer, board[i][j])  # 얘가 왜 필요한 로직인지 이해해야함
#     return answer ** 2

def solution(board):
    ss = {}
    answer = 0
    for y, line in enumerate(board):
        for x, v in enumerate(line):
            if v == 'X':
                continue
            ss[(x,y)] = s = min(
                ss.get((x-1,y), 0),
                ss.get((x,y-1), 0),
                ss.get((x-1,y-1), 0)
            ) + 1
            answer = max(answer, s ** 2)
    return answer


print(solution(board))
