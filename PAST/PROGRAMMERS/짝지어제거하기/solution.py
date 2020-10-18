# 1. deque를 만든다.
# 2. 차례대로 append 하면서 앞뒤 같은 것을 비교
# 3. 있다면 pop()시킨다(2번). popleft아님
# 4. 모든 s를 돌때까지 반복

from collections import deque
def solution(s):
    queue = deque()
    queue.append('.')
    for word in s:
        queue.append(word)
        if queue[-1] == queue[-2]:
            queue.pop()
            queue.pop()
    queue.pop()
    # if len(queue) == 0:
    #     return 1
    # else:
    #     return 0
    return 1 if not queue else 0
def solution(s):
    queue = deque()
    for word in s:
        # 이 조건을 많이 쓰네, if queue and blah blah
        if queue and queue[-1] == word:
            queue.pop()
        else:
            queue.append(word)
    return 1 if not queue else 0
