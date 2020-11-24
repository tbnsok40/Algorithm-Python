from collections import deque
def solution(priorities, location):
    temp = deque([])
    count = 0
    for idx, i in enumerate(priorities):
        temp.append((i, idx))
    # list comprehension을 습관화 하자


    while True:
        head = temp.popleft()
        if head[0] < max(priorities):
            temp.append(head)
        else:
            priorities.remove(max(priorities))
            count += 1
            if head[1] == location:
                return count

    # 못나갈수도있는지 체크하기

priorities = [2, 1, 3, 2]

location = 2
# return 1

# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
# return 5

print(solution(priorities, location))