import sys

N = int(sys.stdin.readline().rstrip())
memo = [0] * (N + 1)

for i in range(2, N + 1):
    memo[i] = memo[i - 1] + 1

    if (i % 2) == 0:
        memo[i] = min(memo[i], memo[i // 2] + 1)
    if (i % 3) == 0:
        memo[i] = min(memo[i], memo[i // 3] + 1)
print(memo[N])

# 이전 풀이와 달리 시간초과가가 안난 이유.
# 우선 재귀를 사용하지 않고도 해결 가능했다.
# 파이썬의 재귀는 느리다더만 진짜이늗ㅅ


"""
3으로 나누어 떨어지면, 3으로 나눈다.
2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

그래서 1을 만든다.

"""
