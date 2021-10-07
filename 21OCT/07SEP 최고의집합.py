def solution(n, s):
    # n 개의 숫자를 더해서 s 를 만들기
    # n = 2
    # temp = []
    # for i in range(1, s):
    #     temp.append((i, s - i))
    # 5개의 자연수로 10 을 만드는 방법
    # 10 - 1, 9 - 1, 8
    # 1을 여러번 빼도 된다. 중복 허용.
    # i = 1
    # while i < s:
    answer = []
    base = s // n
    remain = s % n
    print(base, remain)
    for _ in range(n - remain):
        answer.append(base)
    print(answer)

        


    # print(temp)

    return answer


# 각 원소는 같은 값일 수 있다.
# 더할 원소는 꼭 2개일 필요는 없다. n 개이다.
print(solution(2, 8))
