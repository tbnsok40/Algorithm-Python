# 예외 케이스 뭘까

def check_odd(number):
    if number % 2 != 0:
        return True

def solution2(n,a,b):
    # a, b를 절반으로 줄였을 때, 새로 번호를 부여해야한다.
    count = 1
    while a != b:

        if abs(a - b) == 1:
            return count

        if check_odd(a):
            a += 1
        if check_odd(b):
            b += 1

        n, a, b = n//2, a // 2, b // 2
        count += 1

n = 4
a, b = 1, 4
def solution(n, a, b):
    count = 0
    while a != b:
        a, b = (a+1)//2, (b+1)//2
        count += 1
    return count

print(solution(n, a, b))