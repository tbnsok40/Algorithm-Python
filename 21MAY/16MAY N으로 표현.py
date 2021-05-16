def solution(N, number):

    if N == number:
        return 1
    s = [set() for x in range(8)]

    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:  # j개를 이용하여 만든 수의 집합
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        print(s[i])
        if number in s[i]:

            answer = i + 1
            break
    else:
        answer = -1

    return answer


# 동적 프로그래밍
# 조건을 맞출 때 까지 계속 연
print(solution(5, 12))
