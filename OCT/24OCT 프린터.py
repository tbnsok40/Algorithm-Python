# 처음 시도한 풀이
# from collections import deque
# def solution(priorities, location):
#     priorities[location] = hash(priorities.index(priorities[location]))
#     befor = priorities[:priorities.index(max(priorities))]
#     after = priorities[priorities.index(max(priorities)):]
#     re = after+befor
#     for idx, i in enumerate(re):
#         if i == priorities[location]:
#             return idx + 1

def solution(priorities, location):
    from collections import deque
    temp = deque([(value, idx) for idx, value in enumerate(priorities)])
    count = 0
    while temp:
        first = temp.popleft()
        if temp and first[0] < max(temp)[0]:
            temp.append(first)
        else:
            count += 1
            if first[1] == location:
                return count

priorities = [2, 1, 3, 2]
location = 2
priorities = [1, 1, 9, 1, 1, 1]
location = 0
# 왜 if temp가 필요한지 생각
print(solution(priorities,location))