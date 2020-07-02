N,M,K = map(int, input().split())
temp = [[0]*(M+1) for _ in range(N+1)]

for _ in range(K):
    i, j = map(int, input().split())
    temp[i][j] = 1


v = []

for n in range(1,N):
    for m in range(1,M):
        if temp[n][m] == 1:
            temp[n-1][m]
            temp[n][m-1]
            temp[n][m+1]
            temp[n+1][m]