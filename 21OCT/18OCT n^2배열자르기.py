from itertools import chain

# 1
# def solution(n, left, right):
#     flatten = [[row] * row + [num for num in range(row + 1, n + 1)] for row in range(1, n + 1)]
#     return list(chain(*flatten))[left: right + 1]

# 2
# def solution(n, left, right):
#     b_l, r_l = divmod(left, n)
#     b_r, r_r = divmod(right, n)
#     sum = []
#     for c in range(r_l, n):
#         sum += [max(b_l, c) + 1]
#     for r in range(b_l + 1, b_r):
#         for c in range(n):
#             sum += [max(r, c) + 1]
#     for c in range(r_r + 1):
#         sum += [max(b_r, c) + 1]
#     return sum


#3
def solution(n, left, right):
    total = []
    for i in range(left, right + 1):
        r, c = divmod(i, n)
        total += [max(r, c) + 1]
    return total

# n 이 엄청 크다. 이중 for 문 돌릴 수 없다.
n = 4
left = 7
right = 14
print(solution(n, left, right))
