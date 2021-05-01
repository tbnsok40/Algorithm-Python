from itertools import combinations
def solution(info, query):
    N = len(info)
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