clothes = [['yellow_hat', 'headgear'],
           ['blue_sunglasses', 'eyewear'],
           ['green_turban', 'headgear'],
            ['jeans','pants']]

# dict 생성
def make_dict(clothes):
    cloth_dict = dict()
    for i in (clothes):
        try:
            cloth_dict[i[1]] += 1
        except KeyError:
            cloth_dict[i[1]] = 1
    return cloth_dict

def solution(clothes):
    dict_set = make_dict(clothes)
    values = list(map(int, dict_set.values()))
    ans = 1
    for val in values:
        ans *= (val+1)
    # answer = 0
    # for i in range(1,len(dict_set.keys())+1):
    #     if i == 1:
    #         answer += sum(values)
    #         print('1:',answer)
    #     elif i == 2:
    #         for j in range(len(values)):
    #             for k in range(j+1, len(values)):
    #                 answer += (values[j]*values[k])
    #         print('2:',answer)
    #     elif i ==3:
    #         for j in range(len(values)):
    #             for k in range(j+1, len(values)):
    #                 for l in range(k+1, len(values)):
    #                     answer += (values[j]*values[k]*values[l])
    #         print('3:',answer)
    #     else:
    #         answer += (values[0]*values[1]*values[2]*values[3])
    #         print('4:',answer)
    return ans-1

print(solution(clothes))





    # print(cloth_dict)
    # print(len(cloth_dict.keys()))
    # values = (list(map(int, cloth_dict.values())))
    # sum = 0
    # for i in range(len(cloth_dict.keys())):
    #     if i == 1:
    #         sum = values.sum()
    #     elif i == 2:
    # return dict_set


# 0. 종류 파악 => N
# 1. 한 벌씩만 입는 경우
# 2.
