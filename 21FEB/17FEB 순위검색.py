from itertools import combinations
from collections import defaultdict
def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for _info in info:
        _info = _info.split()
        info_key = _info[:-1]
        info_value = int(_info[-1])
        for i in range(5):
            for c in combinations(info_key,i):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_value)
    # TLL
    for key in info_dict.keys():
        info_dict[key].sort()

    for _query in query:
        _query = _query.split()
        query_score = int(_query[-1])
        _query = _query[:-1]
        for i in range(3):
            _query.remove('and')
        while '-' in _query:
            _query.remove('-')
        tmp_query = ''.join(_query)
        if tmp_query in info_dict:
            scores = info_dict[tmp_query]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if (scores[mid]) >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
            else:
                answer.append(0)
            print(answer)

    return answer
info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))


# 점수를 맨 앞으로 빼던 하여, 점수끼리 먼저 비교하고 애초에 비교할 필요없으면 break