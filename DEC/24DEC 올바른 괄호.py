# 짝지어 제거하기와 비슷한 계열

def solution(s):
    temp = []
    for i in s:
        if i == ')' and not temp:
            return False
        elif i == '(':
            temp.append(i)
        else:
            temp.pop()

    if not temp: return True
    else: return False
