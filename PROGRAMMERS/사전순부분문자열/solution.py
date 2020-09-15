s = 'yzxb'
from itertools import combinations
def solution(s):
    s = list(s)
    result, temp = [], []
    # 문제점 1 : 굳이 조합을 쓰려했다. 결과적으로 조합의 결과가 필요한 건 맞았지만,
    # 과정에서 꼭 조합으로 접근할 필요가 없었다. 그리고 결정적으로 이 과정이 시간 초과를 만들었다.
    list2 = map(list, (combinations(s, i) for i in range(1, len(s) + 1)))

    # 특별한 순서를 원한게 아니었다. 그냥 주어진 문자열에서 슬라이싱을 해도 되는 문제였고

    for li in list2:
        (temp.extend(li))
    for element in temp:
        result.append(('').join(element))
    result.sort()
    return str(result[-1])

def solution(s):
    stack = []
    for char in s:
        while stack and stack[-1] < char:
            stack.pop()
        stack.append(char)
        print(stack)
    return ''.join(stack)

print(solution(s))
