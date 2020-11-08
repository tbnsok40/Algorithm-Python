# 내풀이
def solution(n):
    return sum([int(i) for i in str(n)])

# 다른사람 재귀적 풀이
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10)

n = 1234
print(solution(n))