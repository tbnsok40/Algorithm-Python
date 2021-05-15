# N-Queen은 유일한 백트랙킹 문제
# 모든 경우의 수를 구하면서 필요없는 부분을 가지치기한다.
# 백트랙킹은 n이 작을 때 or 어쩔 수 없이 모든 경우의 수를 구해야 할 때 사용
# 백트랙킹은 재귀를 많이 사용


def solution(n: int):
    return search([0] * n, 0)


def search(queen: list, row: int):
    n = len(queen)
    count = 0

    if n == row:
        return 1

    for col in range(n):
        queen[row] = col
        if check(queen, row):
            count += search(queen, row + 1)
    return count


def check(queen: list, row: int):
    for i in range(row):
        if queen[i] == queen[row] or abs(queen[i] - queen[row]) == row - i:
            return False

    return True
