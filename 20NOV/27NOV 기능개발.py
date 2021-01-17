import math
from collections import deque

# deque than slicing
def solution(progresses, speeds):

    temp = [100 - i for i in progresses]
    sub = deque([math.ceil(a/b) for a, b in zip(temp, speeds)])
    result = []

    while sub:
        count = 1
        head = sub.popleft()
        while sub:
            try:
                if head >= sub[0]:
                    count += 1
                    sub.popleft()
                else:
                    result.append(count)
                    break
            except:
                pass
    result.append(count)
    return result

# 더 깔끔하게 안되나?