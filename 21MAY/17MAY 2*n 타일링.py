
n = 5
# n <= 60000


def solution(n):
    a, b = 1, 2
    for _ in range(2, n):
        a, b = b, a + b
    return b


print(solution(n))
