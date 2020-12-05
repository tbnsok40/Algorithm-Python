
clothes = [["yellow_hat", 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
# clothes = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]

def solution(clothes):
    cloth_dict = dict()
    for cloth, type in clothes:
        try:
            cloth_dict[type] += 1
        except:
            cloth_dict[type] = 1

    # temp = []
    # for i in cloth_dict.values():
    #     temp.append(i)
    temp = list(map(int, cloth_dict.values()))

    ans = 1
    for t in temp:
        ans *= (t + 1)

    return ans - 1

print(solution(clothes))
