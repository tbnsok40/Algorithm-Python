N = int(input())

for _ in range(N):
    cmd = input()
    M = int(input())
    Arr = input()
    try:
        _list = list(map(int, Arr[1:-1].split(',')))
    except ValueError:
        print("error")
        continue

    flag = True
    for i in cmd:
        if i == "R":
            _list = _list[::-1]
            continue
        if i == "D" and _list:
            _list = _list[1:]
        else:
            flag = False
            print("error")
            break
    if flag:
        print(_list)

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
