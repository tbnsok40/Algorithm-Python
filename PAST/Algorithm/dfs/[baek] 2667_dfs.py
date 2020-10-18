import sys
def read(): return sys.stdin.readline().strip()

n = int(read())
matrix = [list(map(int, list(read()))) for _ in range(n)]

aboutX = [1,-1,0,0]
aboutY = [0,0,1,-1]

def dfs(matrix, count, x, y):
    matrix[x][y] = 0
    for i in range(4):
        dX = x + aboutX[i]
        dY = y + aboutY[i]
        if (dX >= 0) & (dY>=0) & (dX< n) & (dY < n):
            if matrix[dX][dY] == 1:
                count = dfs(matrix, count+1, dX, dY)
    return count

ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            ans.append(dfs(matrix, 1, i, j))

print('group number: ',len(ans))
for i in sorted(ans):
    print(i)
