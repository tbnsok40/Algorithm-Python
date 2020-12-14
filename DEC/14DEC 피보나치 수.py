n = 100
def solution(n):
    if n <= 2:
        return 1
    elif n >= 1234567:
        return (solution(n - 1) + solution(n - 2)) % 1234567
    return (solution(n - 1) + solution(n - 2)) % 1234567
print(solution(n))
# 기본적으로 파이썬은 재귀함수에 시간이 많이 걸린다.


# n번째를 1234567로 나눈 나머지를 리턴하라
# 1. n번째 수 x가 1234567보다 작으면 걍 x리턴
# 2. 리턴값은 1234567보다 클 수 없다. answer = 0 ~ 1234566

# 반면 아래 방법은 메모리도 시간도 많이 소모하지 않는다.
# 피보나치를 이렇게도 풀 수 가 있구나
def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a % 1234567

print(solution(n))