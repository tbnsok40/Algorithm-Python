# 런타임 에러
# def solution(n, lost, reserve):
#
#     # + - 해주는 루프 만들고, 결과값이 lost안에 있으면 제거
#     # 다돌리고, n - len(lost)
#     temp = reserve
#     for i in range(len(reserve)):
#         if reserve[i] in lost:
#             temp.remove(reserve[i])
#
#     for i in range(len(temp)):
#         result1 = temp[i] - 1
#         result2 = temp[i] + 1
#         if result1 in lost:
#             lost.remove(result1)
#             continue
#         elif result2 in lost:
#             lost.remove(result2)
#             continue
#
#     return n - len(lost)


# def solution(n, lost, reserve):
#
#     return answer

# 걍 망한 풀이
# def solution(n, lost, reserve):
#     temp = reserve
#     for i in reserve:
#         if i in lost:
#             temp.remove(i), lost.remove(i)
#     for i in temp:
#         plus = i + 1
#         minus = i - 1
#         if plus in lost:
#             lost.remove(plus)
#             continue
#         elif minus in lost:
#             lost.remove(minus)
#             continue
#     return n - len(lost)

# 중복이 없다 -> set()활용 가능
# 왼쪽부터 if검사를 해야한다. 오른쪽부터하면 의미가 없다.

def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)
    return n - len(set_lost)

# 11번케이스 반례
n = 7
lost = [3,5]
reserve = [4,6]
print(solution(n,lost,reserve))
