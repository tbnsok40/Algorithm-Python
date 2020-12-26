# from itertools import combinations
# # number의 순서를 바꾸면 안된다.
# def solution(number, k):
#     number = list(number)
#     N = len(number)
#     M = N - k
#     result = [''.join(i) for i in combinations(number, M)]
#     result.sort()
#     return result[-1]


def solution(number, k):
    result = []
    print(number)
    for idx, i in enumerate(number):
        while len(result) > 0 and i > result[-1] and k > 0:
            print(result, k)
            result.pop()
            k -= 1

        if k == 0:
            result += list(number[idx:])
            break

        result.append(i)

    result = result[:-k] if k > 0 else result

    return ''.join(result)

number = '1842923'
k = 3
print(solution(number, k))
