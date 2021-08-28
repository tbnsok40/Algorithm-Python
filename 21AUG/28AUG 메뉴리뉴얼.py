from itertools import combinations


def solution(orders, course):
    answer = []
    # menu = dict() # initialize
    for n in course:  # 얘가 먼저 나와야 하는 이유는, 갯수별 최강자를 먼저 골라내야하기 때문
        menu = dict()
        for order in orders:
            for combi in combinations(order, n):
                combi = sorted(combi)
                menu_candidate = ''.join(combi)
                try:
                    menu[menu_candidate] += 1
                except KeyError:
                    menu[menu_candidate] = 1
        max = 2
        for m, n in menu.items():
            if n >= max:
                max = n
        for m, n in menu.items():
            if n == max:
                answer.append(m)
    answer.sort()
    return answer




orders = ["XYZ", "XWY", "WXA"] # # ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))
