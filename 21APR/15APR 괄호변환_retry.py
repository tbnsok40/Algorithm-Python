from collections import deque


def reverse(sentence):
    # return sentence[::-1] 은 그냥 문자열의 순서를 뒤집는 것 뿐, 각 괄호의 방향을 뒤집는 것과는 다르다.
    return ''.join([')' if s == '(' else '(' for s in sentence])


def detach(sentence):
    temp_que = deque(sentence)
    left, right = 0, 0
    u, v = '', ''

    while temp_que:
        u += temp_que.popleft()
        if u[-1] == "(":
            left += 1
        else:
            right += 1

        if left == right:
            break

    v = ''.join(list(temp_que))
    return u, v


def recursive(sentence):
    if sentence == '':
        return ''
    u, v = detach(sentence)
    if correct(u):
        return u + recursive(v)
    else:
        # return '(' + recursive(v) + ')' + reverse(u[1:-1])
        return '(' + recursive(v) + ')' + ''.join(list(map(lambda x: ")" if x =="(" else "(", u[1:-1])))


def correct(sentence):
    stack = []
    for sen in sentence:
        if sen == "(":
            stack.append(sen)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return True if len(stack) == 0 else False


def solution(p):
    return p if correct(p) else recursive(p)

p = ")("

print(solution(p))


"""
p를 어떻게 u,v로 나눌 것인지
p의 인덱스를 점차 높혀가며, 우선 correct() True인지, balance() TRUE인지 체크 (둘중 하나는 True 나올 때까지 인덱스 계속 높인다)
1) 우선 u,v 모두 균형잡힌 문자열인지 체크
2) 그런 후 u의 Correct()를 체크 -> 맞으면 v를 다시 solution()재귀에. -> 아니면 다음 로직 실
1) Correct() true이면, v를 다시 solution()에 재귀
2) Balance()True이면, 다음 로직 들어가기. => 이것도 따로 함수를 파면 좋을 것 같아. 
"""

"""
일단 p는 무조건 균형잡힌 문자열임. 
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.  -=> 아 하나하나를 다 뒤집어라는 뜻이구
  4-5. 생성된 문자열을 반환합니다.
"""