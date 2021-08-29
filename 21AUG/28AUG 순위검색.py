from itertools import combinations, product
from collections import defaultdict


# info_dict가 리스트야 하는걸 인지 못함.
def solution(info, query):
    result = []
    info_dict = {}

    for info_ in info:
        inf = info_.split(' ')
        temp = [(inf[0], '-'), (inf[1], '-'), (inf[2], '-'), (inf[3], '-')]
        product_temps = list(product(*temp))
        for product_temp in product_temps:
            case = ''.join(product_temp)
            if case in info_dict:
                info_dict[case].append(int(inf[4]))
            if case not in info_dict:
                info_dict[case] = [int(inf[4])]

    for key in info_dict.keys():
        info_dict[key].sort()

    for query_ in query:
        query_ = query_.split(' ')
        query_score = int(query_[-1])
        query_info = query_[:-1]

        while 'and' in query_info:
            query_info.remove('and')
        query_info = ''.join(query_info)

        if query_info in info_dict:
            scores = info_dict[query_info]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (end + start) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                result.append(len(scores) - start)
        else:
            result.append(0)

    return result


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
solution(info, query)
# result = [1, 1, 1, 1, 2, 4]
