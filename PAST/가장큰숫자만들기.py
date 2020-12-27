number = '1842923'
k = 3

# number의 순서를 바꾸면 안된다.
# combinations를 쓰면 조진다. 시간복잡도에서 걸린다.

from itertools import combinations
def solution(number, k):
    number = list(number)
    N = len(number)
    M = N - k
    result = [''.join(i) for i in combinations(number, M)]
    result.sort()
    return result[-1]

# k 수 만큼 number에서 숫자를 제거하여, 가장 큰 수를 만들어야한다.
# 그래서 처음엔 조합으로 접근해야 한다고 생각했다.
#
def solution(number, k):
    result = []
    for idx, i in enumerate(number):
        while len(result) > 0 and i > result[-1] and k > 0:
            result.pop()
            k -= 1
        if k == 0:
            result += list(number[idx:])
            break
        result.append(i)

    if k > 0:
        result = result[-k]
    else:
        result = result

    return ''.join(result)

print(solution(number, k))
