# 초기 시도
def solution(n):
    answer = ''
    a,b = divmod(n,3)
    answer += str(b)
    while a > 1:
        a, b = divmod(a,3)
        answer += str(b)
        if a == 1:
            answer += str(a)
    result = 0
    for idx, n in enumerate(answer):
        result += (int(n)* 3 ** (len(answer)-(idx + 1)))
    return result

# 코드 정리
def solution(n):
    answer, result = '', 0
    # n이 1일 때 처리안해주면 에러
    if n == 1:
        return 1
    while n > 1:
        a,b = divmod(n,3)
        answer += str(b)
        if a == 1:
            answer += str(a)
            break
        n = a

    for idx, n in enumerate(answer):
        result += (int(n)* 3 ** (len(answer)-(idx + 1)))
    return result

print(solution(1))