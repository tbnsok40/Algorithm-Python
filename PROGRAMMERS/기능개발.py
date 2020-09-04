progress = [93,30,55]
speeds = [1,30,5]
import math
from collections import defaultdict
def solution(progress, speeds):
    # 남은 작업량 딕셔너리에 저장
    # dic = defaultdict(list)
    # for i, idx in enumerate(progress):
    #     dic[i].append(math.ceil((100 - idx)/speeds[i]))
    dic = [7,3,2,1,7]
    dic = [7,8,5,4,7,9,6]
    i, count = 0,1
    result = []
    while dic:
        print('dic ',dic)
        print('result ',result)
        if dic[i] >= dic[i+1]:
            count += 1
            dic.pop(0)
        else:
            result.append(count)
            count = 1
            dic.pop(0)


    return result
print(solution(progress,speeds))

