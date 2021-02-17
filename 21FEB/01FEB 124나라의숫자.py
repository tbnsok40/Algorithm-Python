# 패턴을 보면 3을 단위로  1의 단위에선 같은 숫자가 반복된다. => 재귀가 하나의 방법이 될 수 있다,
def solution(n):
    if n <= 3:
        return '124'[n-1]
    else:
        a, b = divmod(n - 1, 3)
        return solution(a) + '124'[b]

# 반복으로도 풀 수 있다
def solution(n):
    num = '124'
    answer = ''
    while n > 0:
        p, r = divmod(n - 1, 3)
        answer = num[r] + answer
        n = p
    return answer

print(solution(27))