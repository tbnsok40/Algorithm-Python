def solution(info, query):
    N = len(info)
    info_dict = {}  # info length에 맞게 dict 내부 객체 생성, key: numbers
    query_dict = {}
    for idx, i in enumerate(info):
        j = i.split(' ')
        info_dict[idx] = {
            "lang": j[0],
            "position": j[1],
            "career": j[2],
            "food": j[3],
            'score': j[4]
        }

    for idx, i in enumerate(query):
        j = i.split(' ')
        while 'and' in j:
            j.remove('and')
        query_dict[idx] = {
            "lang": j[0],
            "position": j[1],
            "career": j[2],
            "food": j[3],
            'score': j[4]
        }
    dict_col = ['lang', 'position', 'career', 'food','score']
    result = []
    for i in query_dict:
        count = 0
        for j, k in zip(info_dict, dict_col):
            if (query_dict[i][k] != info_dict[j][k]):
                if query_dict[i][k] == '-':
                    pass
                # try:
                #     if int(query_dict[i][k]) <= int(info_dict[j][k]):
                #         count += 1
                #     else:
                #         break
                # except ValueError as e:
                #     print('except')
                else:
                    break
            print(i,j,k)
        else:
            print('yes')
            # count += 1

        # print(count)
        result.append(count)
        print(result)


            # print(info_dict[k], query_dict[k])
            # if query_dict[lang] == info_dict[lang]:



    # for i in range(N):
    #     for j, k, p in zip(info_dict, query_dict, dict_col):
    #         print(info_dict[i][p], query_dict[i][p])

    # for i,k in zip(N, dict_col):
    #     print(i,k)
    #     if info_dict[i][k] != query_dict[i][k]:
    #         if query_dict[j][k] == '-':
    #             continue
    #         else:
    #             break
    # else:
    #     result.append()

        # print(info_dict[i][k])
        # print(query_dict[j][k])

    # print(info_dict[0]["position"])



    return


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))
