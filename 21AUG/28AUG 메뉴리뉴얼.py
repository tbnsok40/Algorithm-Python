from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    # menu = dict() # initialize
    for n in course:  # 얘가 먼저 나와야 하는 이유는, 갯수별 최강자를 먼저 골라내야하기 때문
        temp = []
        for order in orders:
            for combination in combinations(order, n):
                temp.append(''.join(sorted(combination)))

        menu = Counter(temp)
        try:
            maximum = max(Counter(temp).values())
        except ValueError:
            pass

        for key, value in menu.items():
            if value == maximum and maximum > 1:
                answer.append(key)
    answer.sort()
    return answer




orders = ["XYZ", "XWY", "WXA"] # # ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))
