from collections import deque

N = int(input())

for _ in range(N):
    cmd = input()
    M = int(input())
    Arr = input()
    _list = deque(Arr[1:-1].split(','))

    # 여기 처리를 해주어야 통과할 수 있다.
    if M == 0:
        _list = []

    flag = True
    flag_R = False
    for i in cmd:
        if i == "R":
            if not flag_R:
                flag_R = True
            else:
                flag_R = False
            continue
        if i == "D" and _list:
            if flag_R:
                _list.pop()
            else:
                _list.popleft()
        else:
            flag = False
            print("error")
            break
    if flag:  # error 출력한 경우는, 해당 조건문 불통과
        if flag_R:
            # print(list(_list)[::-1])
            print("[" + ",".join(list(_list)[::-1]) + "]")

        else:
            print("[" + ",".join(_list) + "]")

"""
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
"""
