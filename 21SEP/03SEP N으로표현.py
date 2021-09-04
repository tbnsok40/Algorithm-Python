
def solution(N, number):
    res = [0] * 8
    for i in range(1, 9):
        set_ = set()
        set_.add(int(str(N) * i))
        res[i - 1] = set_

    if N == number:
        return 1

    for i in range(1, 8):  # 1 <= i < 8
        for j in range(i):  # 0 <= j < i
            for op1 in res[j]:
                for op2 in res[i - j - 1]:  # 0 <= (i - j - 1) < 6
                    res[i].add(op1 + op2)
                    res[i].add(op1 - op2)
                    res[i].add(op1 * op2)
                    if op2 != 0:
                        res[i].add(op1 // op2)
            if number in res[i]:
                return i + 1
    else:
        return -1


N = 5
number = 12

print(solution(N, number))
