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
# 조합 접근 자체는 옳았지만 시간복잡도에서 터진다.
# 잘못 생각해서 순열로 접근하려 했는데, number의 순서를 바꾸면 안된다.

# Greedy로 접근
def solution(number, k):
    result = []
    for idx, i in enumerate(number):
        while len(result) > 0 and i > result[-1] and k > 0: # 여기서 k에 대한 조건이 빠지면, k개 이상으로 계속 뺀다.
            result.pop()
            k -= 1 #return할 결과는 result이므로 result에서 하나씩 pop한다는 건 k를 1씩 줄여야 함을 뜻한다

        if k == 0:
            result += list(number[idx:])
            break

        result.append(i)

    # if k > 0:
    #     result = result[:-k]
    # else:
    #     result = result
    result = result[:-k] if k > 0 else result

    return ''.join(result)
