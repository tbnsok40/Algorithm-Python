number = '1231234'
k = 3


def solution(number, k):
    result = []

    for idx, i in enumerate(number):
        while len(result)>0 and i > result[-1] and k > 0:
            result.pop()
            k -= 1

        if k == 0:
            result += list(number[idx:])
            break

        result.append(i)
    result = result[:-k] if k > 0 else result

    return ''.join(result)

print(solution(number, k))

# 스타트업 드라마의 교훈은 할머니가 어린 지평에게 손을 건넨 것으로 시작한다. 손을 건넬줄 아는 것.
