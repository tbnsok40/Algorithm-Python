from itertools import combinations
def solution(info, query):
    N = len(info)
    # dictionary 시도
    # info_dict = {}  # info length에 맞게 dict 내부 객체 생성, key: numbers
    # query_dict = {}
    # for idx, i in enumerate(info):
    #     j = i.split(' ')
    #     info_dict[idx] = {
    #         "lang": j[0],
    #         "position": j[1],
    #         "career": j[2],
    #         "food": j[3],
    #         'score': j[4]
    #     }
    # for idx, i in enumerate(query):
    #     j = i.split(' ')
    #     while 'and' in j:
    #         j.remove('and')
    #     query_dict[idx] = {
    #         "lang": j[0],
    #         "position": j[1],
    #         "career": j[2],
    #         "food": j[3],
    #         'score': j[4]
    #     }
    # dict_col = ['lang', 'position', 'career', 'food', 'score']
    #
    info_list = []
    query_list = []
    for idx, i in enumerate(info):
        info_ele = i.split(' ')
        info_list.append(info_ele)
    for idx, i in enumerate(query):
        query_ele = i.split(' ')
        while 'and' in query_ele:
            query_ele.remove('and')
        query_list.append(query_ele)
    result = []
    for query in query_list:
        count = 0
        for info in info_list:
            for n in range(5):
                if ((query[n] != '-') and (query[n] != info[n]) and n < 4):
                    break

                if ((n == 4) and (int(query[n]) > int(info[n]))):
                    break
            else:
                count += 1

        result.append(count)
    return result
info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))
