# def solution(a, b):
#     if a == b:
#         return a
#
#     sum = 0
#     if a < b:
#         for i in range(a,b+1):
#             sum += i
#     else:
#         for i in range(b, a+1):
#             sum += i
#     return sum

# 아래는 더 간결하게 / range()메서드를 꼭 for문에서만 쓸 필요는 없다.

def solution(a, b):
    if a == b: return a
    if a < b:
        return sum(range(a, b + 1))
    else:
        return sum(range(b, a + 1))
print(solution(10,8))