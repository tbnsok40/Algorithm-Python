import sys


def __main__():
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))

    MAX = max(arr)
    total = 0
    for i in arr:
        total += ((i / MAX) * 100)
    print(total/N)
    return


__main__()

"""
18 2

연속된 수가, N 을 만들 수 있는지. 
N 을 어케 나눌것인
N 이 10억 까지 치솟으므로, 시간복잡도 고려해야한다. 

연속되어야 한다.
"""
