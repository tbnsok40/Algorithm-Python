clothes = [['yellow_hat', 'headgear'],
           ['blue_sunglasses', 'eyewear'],
           # ['green_turban', 'headgear']]
            ['jeans','pants']]

def solution(clothes):

    cloth_dict = dict()
    for i in clothes:
        try:
            cloth_dict[i[1]] += i[0]
        except KeyError:
            cloth_dict[i[1]] = i[0]
    print(cloth_dict)
    return
print(solution(clothes))
# 0. 종류 파악 => N
# 1. 한 벌씩만 입는 경우
# 2. 