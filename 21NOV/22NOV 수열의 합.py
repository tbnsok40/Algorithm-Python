import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def __main__():
    solid_N, L = map(int, input().split())
    s = 0
    flag = False
    while True:
        N = solid_N

        if s >= N:
            print(-1)
            exit(0)
        res = []
        for i in range(s, solid_N//2):
            N -= i
            res.append(i)
            if N == 0 and len(res) >= L:
                flag = True
                break
        s += 1

        if flag:
            print(res)
            break



__main__()

"""
18 2

연속된 수가, N 을 만들 수 있는지. 
N 을 어케 나눌것인
N 이 10억 까지 치솟으므로, 시간복잡도 고려해야한다. 

연속되어야 한다.
"""
