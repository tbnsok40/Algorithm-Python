def solution(N, stages):
    stage_dict = {}
    rate_dict = {}
    for i in stages:
        try:
            stage_dict[i] += 1
        except KeyError:
            stage_dict[i] = 1

    stage_set = sorted(stage_dict.items(), key=lambda x: x[0])
    print(stage_set)
    key_, val_ = stage_set[0]
    rate_dict[key_] = val_ / len(stages)
    temp = val_
    for key, val in stage_set[1:]:
        mod = len(stages)-temp
        print(key, val)
        rate_dict[key] = val / mod
        temp = val
    rate_dict2 = sorted(rate_dict.items(), key = lambda x: x[1], reverse=True)
    print(rate_dict2)
    # for i in (sorted(stage_dict)):
    #     rate_dict[i] = stage_dict[i] / (N)
    #     before = i
    #
    # rate_dict = sorted(rate_dict.items(), key=lambda x:x[1], reverse=True)
    return

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))