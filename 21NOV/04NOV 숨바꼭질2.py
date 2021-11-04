import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append(A)

    while queue:
        value = queue.popleft()
        if value == B:
            print(time[value])
            exit()
        for i in (value + 1, value - 1, value * 2):
            if not time[i] and 0 <= i <= MAX:
                # why not time 조건이 먼저 나오면 indexError가 터짐..?
                # because => i가 time 의 인덱스를 벗어나는 값이 먼저 time[i]에 들어가면 당연히 IndexError 나기 때문
                # 그래서 0 <= i <= MAX 라는 범위 조건이 and 의 선조건이 되야한다.
                time[i] = time[value] + 1
                queue.append(i)


A, B = sys.stdin.readline().split()
A = int(A)
B = int(B)
MAX = 100000
time = [0] * (MAX + 1)

bfs()

"""

5 17

case 1: x - 1, x + 1
case 2: x * 2

"""
