# count 를 어디에 선언하는 것이 맞는지
# def check(r, c, arr):
#     for y, x in arr:
#         if y == r or c == x:
#             break
#         if abs(y - r) == abs(x - c):
#             break
#     else:
#         return True
#
#
# def solution(n):
#
#     for i in range(n):
#         for j in range(n):
#             i, j
#             pass
#     return

def solution(n):
    cases = [0] # shallow copy of the cases (list)

    def dfs(queens, next_queen):
        # column check
        if next_queen in queens:
            return

        # diagonal check
        for row, column in enumerate(queens):
            h = len(queens) - row
            if next_queen == column + h or next_queen == column - h:
                return

        queens.append(next_queen)
        # end check
        if len(queens) == n:
            cases[0] += 1
            return

        for next_queen in range(n):
            dfs(queens[:], next_queen) # deep copy of queens

    for next_queen in range(n):
        queens = []
        dfs(queens, next_queen)
    return cases[0]

n = 4
print(solution(n))
