import sys
def read(): return map(int, sys.stdin.readline().split())
N,m,M,T,R = read()
# 5 70 120 25 15
# N: 운동 시간
# m: 맥박 하한가, 초기 맥박
# M: 맥박 상한가
# T: 운동시 1분마다 추가
# R: 휴식시 1분마다 차감
X = m
recount = 0

if (X + T > M):
    print(-1)
    sys.exit()
while N > 0:
    if (X+T <= M):
        X += T
        N -= 1
        recount +=1
    else:
        if (X-R < m):
            X = m
        else:
            X -= R
        recount += 1
print(recount)


# print(workout(N,m,M,T,R))