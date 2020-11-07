def solution(n):
    # 여기서 list없어도 된다 = str자체로도 [::-1] 가능
    n = list(str(n))[::-1]
    return list(map(int, n))

# [::-1] 대신 reversed() 메서드 사용
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
