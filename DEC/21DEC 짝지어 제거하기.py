from collections import deque

# s가 list면 시간초과, deque()이면 통
def solution(s):
    temp = []
    s = deque(list(s))
    temp.append(s.popleft())
    while s:
        try:
            if temp[-1] == s[0]:
                temp.pop()
                s.popleft()
            else:
                temp.append(s.popleft())
        except:
            temp.append(s.popleft())

    if len(temp) == 0: return 1
    else: return 0
print(solution(s))

# 굳이 try~ except 쓰지 않아도 된다.
def solution(s):
    answer = list()
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if answer[-1] == i:
                answer.pop()
            else:
                answer.append(i)
    if answer:
        return 0
    else: return 1

