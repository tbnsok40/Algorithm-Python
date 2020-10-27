def solution(s):
    s = list(s) # 문자열은 이거 안해도 for문 돌리면 알아서 분리돼서 나와.
    temp = []
    for bracket in s:
        try:
            if bracket == '(':
                temp.append(bracket)
            else:
                temp.pop()
        except IndexError:
            return False
    if temp:
        return False
    else:
        return True

# s = '(())()'
# s = '(())('
# print(solution(s))
