v = [[3, 10],[1, 4],[1, 10]]
v = [[1, 1], [2, 2], [1, 2]]
# from collections import Counter
# def solution(v):
#     answer = []
#     for i in zip(*v):
#         y = Counter(i)
#         print(y)
#         answer.extend([i for i in y if y[i] == 1])
#         # extend : append는 리스트 전체를 [] 형태로 넣고, extend는 []내부의 원소들을 넣는다.
#         print(answer)
#         # print(y)
# print(solution(v))

# # 딕셔너리 만들기

# # 각 좌표가 전체적으로 2개씩 만들어져야해
# from collections import deque
# def solution(v):
#     dic = dict()
#     queue = deque()
#     result = []
#
#     for x, y in v:
#         queue.append(x)
#         queue.append(y)
#         while queue:
#             x = queue.popleft()
#             try:
#                 dic[x] += 1
#             except KeyError:
#                 dic[x] = 1
#
#     for i in dic.keys():
#         if dic[i] == (1):
#             result.append(i)
#         elif dic[i] == 3:
#             result.append(i)
#         else:
#             continue
#
#
#     v.append(result)
#     a = abs(v[0][0] - v[1][0])
#     b = abs(v[2][0] - v[3][0])
#
#     if a == b:
#         return result
#     else:
#         re_result = []
#         for i in result[::-1]:
#             re_result.append(i)
#         return re_result
# print(solution(v))

from collections import Counter
def solution(v):
    # 총 좌표의 x와 y의 갯수는 같아야한다.
    result = []
    for i in zip(*v):
        y = Counter(i)
        result.extend([i for i in y if y[i] == 1])
    return result
print(solution(v))