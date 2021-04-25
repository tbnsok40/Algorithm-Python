# 괄호 회전하기
from collections import deque


def solution(s):
    answer = 0
    s = deque(s)
    if len(s) % 2 != 0:
        return 0

    for i in range(len(s)):
        s.append(s.popleft())
        if is_correct(s):
            answer += 1

    return answer


def is_correct(s):
    bracket = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    opener = ['[', '{', '(']
    s_ = deque(s)
    temp = []
    for i in s_:
        if not temp:
            temp.append(i)
            continue
        try:
            if (i not in opener) and (bracket[temp[-1]] == i):
                temp.pop()
            # 왜 애를 지워야 통과하지..?
            # if (i not in opener) and (bracket[temp[-1]] != i):
            #     return False
            if i in opener:
                temp.append(i)
        except KeyError:
            pass
    if not temp:
        return True
