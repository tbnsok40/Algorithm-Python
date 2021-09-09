def solution(price, money, count):
    answer = sum([(price * i) for i in range(1, count + 1)]) - money
    return answer if answer >= 0 else 0


price = 3
money = 20
count = 4

print(solution(price, money, count))
