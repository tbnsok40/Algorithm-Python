def solution(ings, menu, sell):
    ings_dict, menu_dict = {}, {}
    answer = 0
    for i in ings:
        ing, price = i.split(' ')
        ings_dict[ing] = int(price)

    for m in menu:
        food, ingr, price = m.split(" ")
        ings_price = 0
        for k in ingr:
            ings_price += ings_dict[k]
        menu_dict[food] = int(price) - ings_price

    for s in sell:
        menu, amount = s.split(' ')
        answer += menu_dict[menu] * int(amount)

    return answer


# ings = ["r 10", "a 23", "t 124", "k 9"]
# menu = ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55",
#         "WATER a 20"]
# sell = ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]

ings = ["x 25", "y 20", "z 1000"]
menu = ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"]
sell = ["BBBB 3", "TTT 2"]

print(solution(ings, menu, sell))

"""

"""
