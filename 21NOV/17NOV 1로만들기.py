import sys

N = int(sys.stdin.readline().rstrip())
count = 0
result = []
memo = [0] * (N + 1)


def dp(N, count):
    # if memo[N] != 0:
    #     return
    if N == 1:
        result.append(count)
        return
    if N % 3 == 0:
        dp(N // 3, count + 1)
    if N % 2 == 0:
        dp(N // 2, count + 1)
    return dp(N - 1, count + 1)


dp(N, 0)
print(min(result))
# 시간 초과 => 이걸 메모이제이션으로 변환하면 시간초과를 해결할 수 있지 않을까.


"""
3으로 나누어 떨어지면, 3으로 나눈다.
2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

그래서 1을 만든다.

"""
