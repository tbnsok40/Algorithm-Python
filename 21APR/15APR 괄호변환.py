from collections import defaultdict


def balance(string):
    balan = defaultdict(int)
    for s in string:
        balan[s] += 1

    # strrr = map(lambda s: balan[s] + 1, string)
    if balan[')'] == balan['(']:
        return True
    else:
        return False


def correct(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0


answer = ''


def solution(p):
    global answer
    for idx in range(1, p):
        if balance(p[:idx]) and balance(p[idx:]):
            if correct(p[:idx]):
                answer += p[:idx]
                return solution(p[idx:])
            # 아 리턴이 곧 브레이크 역할이네, 아닌가?
            else:
                temp = '('
                solution(p[idx:])
                # 다음 로직 함수 실행

    return answer


print()


# 함수 두개 생성
# 올바른 문자열인지 검사하는 함수
# 균형잡힌 문자열인지 검사하는 함수
# 둘다 boolean 반환하도록


"""
p를 어떻게 u,v로 나눌 것인지
p의 인덱스를 점차 높혀가며, 우선 correct() True인지, balance() TRUE인지 체크 (둘중 하나는 True 나올 때까지 인덱스 계속 높인다)
1) 우선 u,v 모두 균형잡힌 문자열인지 체크
2) 그런 후 u의 Correct()를 체크 -> 맞으면 v를 다시 solution()재귀에. -> 아니면 다음 로직 실
1) Correct() true이면, v를 다시 solution()에 재귀
2) Balance()True이면, 다음 로직 들어가기. => 이것도 따로 함수를 파면 좋을 것 같아. 
"""