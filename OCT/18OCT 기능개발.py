progresses = [93,30,55]
speeds = [1,30,5]

import math
def solution(progresses, speeds):
    rest = [math.ceil((100 - p)/s) for p,s in zip(progresses, speeds)]
    count, i = 1, 1
    answer = []
    while rest:
        try:
            if rest[0] >= rest[i]:
                count += 1
                i += 1
            else:
                rest = rest[i:]
                answer.append(count)
                count, i = 1, 1
        except IndexError:
            answer.append(count)
            break
    return answer

# try ~ except 내부에 if ~ else 구문 사용
# 리스트 슬라이싱,