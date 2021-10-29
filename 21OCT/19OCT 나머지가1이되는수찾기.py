from math import sqrt


def solution(n):

    # 무식하게 소수를 증명하는 방법은 for 루프 돌리는 것
    # 다른 방법 => 제곱근 사용 : 왜그런걸까 원리가 뭐야 => 블로그쓰자.
    def prime_number(n):
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        else:
            return True
    temp = n - 1
    if prime_number(temp):
        return temp
    else:
        for i in range(2, temp):
            if temp % i == 0:
                return i
    # if temp 가 소수
    # return temp

# 192 => 191

# 21 , 2 => 21 - 1 = 20 => 20의 1이 아닌 최소약수: 2
# 30, 29
# 반례 26 => 5로 나누어 떨어지는 경우도 생각해야.
print(solution(26))

# 소수: 2, 3, 5, 7, 11, 13, 17, 19, 23,

