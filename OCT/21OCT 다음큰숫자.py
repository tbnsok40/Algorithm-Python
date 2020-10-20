# 함수를 기능별로 여러개 만들어서 생각하기
# 1. 이진법으로 바꿔야한다.
# 2. 자기보다 큰 숫자를 돌려야한다.
# 3. 이진법의 1을 세야한다.
# 3. 두 숫자를 비교해야한다.

def solution(n):
    first = to_binary(n)
    first_count = counting_one(first)
    for i in range(n+1, 1000000):
        second = to_binary(i)
        if first_count == counting_one(second):
            return i

def to_binary(n):
    if n < 2:
        return '01'[n]
    else:
        a, b = divmod(n, 2)
        return to_binary(a) + '01'[b]

def counting_one(n):
    n = str(n)
    return n.count('1')

print(solution(10))
