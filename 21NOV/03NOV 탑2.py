import sys

N = sys.stdin.readline().rstrip()
M = list(map(int, sys.stdin.readline().split()))
result = [0] * int(N)
stack = []
for i in range(len(M)):

    while stack and M[stack[-1]] < M[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1

    stack.append(i)

print(*result)

"""
5
4 6 5 7 4
6 9 5 7 4

# 역으로 정렬?

"""
