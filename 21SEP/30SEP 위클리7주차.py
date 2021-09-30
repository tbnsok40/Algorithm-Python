from collections import deque, defaultdict


def solution(enter, leave):
    enter_queue = deque(enter)
    leave_queue = deque(leave)
    queue = deque()
    entire_dict = defaultdict(list)
    # print(queue)
    while enter_queue:
        ent = enter_queue.popleft()
        queue.append(ent)
        # append 했으면 딕셔너리 갱신
        for q in queue:
            entire_dict[q] += [set(queue)]
        # print(entire_dict)
        # while leave_queue[0] in queue:
        while leave_queue:
            if leave_queue[0] in queue:
                lea = leave_queue.popleft()
                queue.remove(lea)
            else:
                break
    result = defaultdict(set)
    answer = [0] * len(enter)
    for k, v in entire_dict.items():
        for val in v:
            result[k] = result[k].union(val) - {k}
        # print(k, len(result[k]))
        answer[k - 1] = len(result[k])
    return answer
# enter = [1, 3, 2]
# leave = [1, 2, 3]

enter = [1,4,2,3]
leave = [2,1,3,4]


print(solution(enter, leave))
