# N, M = map(int, input().split())
#
# a = []
# for _ in range(N):
#     li = list(map(int, input().split()))
#     a.append(li)
#
#
# for _ in range(int(input())):
#     i,j,x,y = map(int, input().split())
#     i -= 1
#     j -= 1
#     x -= 1
#     y -= 1
#     sum = 0
#
#     for n in range(i, x+1):
#         for m in range(j, y+1):
#             sum += a[n][m]
#             # print(n,m,sum)
#     print(sum)

# n, m = map(int, input().split())
# a = []
# dp = [[0] * (m + 1) for _ in range(n + 1)]
# for _ in range(n):
#     a.append(list(map(int, input().split())))
# print('a:',a)
# print('dp:',dp)
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         dp[i][j] = a[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
# print('updated dp:',dp)
# k = int(input())
# for _ in range(k):
#     i, j, x, y = map(int, input().split())
#     print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])
import sys

N, M = map(int, sys.stdin.readline().split())
temp = [[0]*(M+1) for _ in range(N+1)]
li = []
for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, M+1):
        temp[i][j] = li[i-1][j-1] + temp[i-1][j] + temp[i][j-1] - temp[i-1][j-1]

for _ in range(int(input())):
    i,j,x,y = map(int, sys.stdin.readline().split())
    print(temp[x][y] - temp[x][j-1] -temp[i-1][y] + temp[i-1][j-1])

