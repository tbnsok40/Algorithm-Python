from itertools import combinations
def solution(orders, course):
    orders.sort()
    word_dict = {}
    for i in orders:
        for j in range(2, len(i) + 1):
            for k in combinations((i), j):
                k = ''.join([*(k)])
                # print(k)
                try:
                    word_dict[k] += 1
                except:
                    word_dict[k] = 1
    result = []
    for i in word_dict.keys():
        if word_dict[i] > 1:
            result.append((word_dict[i], i))
    # result.sort()
    # print(word_dict)
    print(result)
    return


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))