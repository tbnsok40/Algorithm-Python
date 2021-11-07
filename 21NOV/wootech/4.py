from collections import deque


def solution(s):
    if len(set(s)) == 1:
        return [len(s)]
    # 원형 큐 기준 같은 녀석들끼리 묶었다. 근데 만약 모든 글자가 같다면? => if 로 필터링 먼저 쳐주자
    queue = deque(s)
    while True:
        head = queue.popleft()
        if head == queue[-1]:
            queue.append(head)
        else:
            queue.appendleft(head)
            break

    count = 1
    result = []
    for idx, i in enumerate(queue):
        if idx != len(queue) - 1:
            if i == queue[idx + 1]:
                count += 1
            else:
                result.append(count)
                count = 1
        else:
            if queue[idx - 1] == i:
                pass
            else:
                count = 1
            result.append(count)
    return sorted(result)


s = "wowwow"
print(solution(s))
