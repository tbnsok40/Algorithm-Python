import sys

N = int(sys.stdin.readline().rstrip())
base = N // 2


def countEach(base):
    small = 0
    for i in (str(base)):
        small += int(i)
    return small


def __main__():
    result = []
    for k in range(base, N):
        if k + countEach(k) == N:
            result.append(k)
    if len(result) > 0:
        print(min(result))
    else:
        print(0)


__main__()

""" 
245 => 245 + 2 + 4 + 5 = 256
245는 256의 생성자
생성자 없는 경우 존재. 생성자 여러개인 존재도 존재
가장 작은 생성자를 구하라. 
"""
