# progresses = [93,30,55]
# speeds = [1,30,5]
import math
def solution(progresses, speeds):
    answer = list()
    # 남은 작업량 리스트에 저장 => list comprehension
    rest = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    count = 1
    max_rest = rest[0]

    for i in range(1, len(rest)):
        if max_rest >= rest[i]:
            count += 1
        else:
            answer.append(count)
            max_rest = rest[i]
            count = 1
    answer.append(count)
    return answer