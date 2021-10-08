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
    if s < n:
        return [-1]

    base, remain = divmod(s, n)
    answer = [base for _ in range(n)]

    for idx in range(remain):
        answer[idx] = base + 1

    return sorted(answer)
