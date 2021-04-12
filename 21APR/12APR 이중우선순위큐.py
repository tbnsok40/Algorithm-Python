# operations = ["I 7", "I 5", "I -5", "D -1"]
operations = ["I 16","D 1"]


# 틀린 이유: 순서 무시, insert 모두 처리 후, delete 하면, 순서가 무시돼서 틀린다.
# def solution(operations):
#     # I 는 무조건 넣고, D는 무조건 뺀다
#     temp, plus, minus = [], 0, 0
#     for i in operations:
#         a, b = i.split(" ")
#         if a == "I":
#             temp.append(int(b))
#         elif a == 'D' and b == '1':
#             plus += 1
#         else:
#             minus += 1
#     if plus + minus >= len(temp):
#         return [0, 0]
#     # 최소 힙 처리
#     heapq.heapify(temp)
#     for _ in range(minus):
#         heapq.heappop(temp)
#     min_ = heapq.heappop(temp)
#     max_heap = []
#     heapq.nlargest(1)
#     # 최대 힙 만들기
#     for num in temp:
#         print(num)
#         heapq.heappush(max_heap, (-num, num))
#     # 최대 힙 상태
#     for _ in range(plus):
#         heapq.heappop(max_heap)
#     max_ = heapq.heappop(max_heap)[1]
#     return [max_, min_]


# 2번째 시도
# import heapq
# def solution(operations):
#     temp, max_ = [], []
#     for num in operations:
#         a, b = num.split(' ')
#         if a == 'I':
#             temp.append(int(b))
#         if a == "D" and b == '-1':
#             heapq.heappop(temp)
#         if a == 'D' and b == '1':
#             try:
#                 temp.remove(heapq.nlargest(1, temp)[0])
#             except IndexError:
#                 pass
#     if temp:
#         return [*heapq.nlargest(1, temp), heapq.heappop(temp)]
#     else:
#         return [0, 0]


# 핵심은 nlargest(), nsmallest(), list.index()
# remove는 IndexError 터지기 쉽다. pop을 사용하자 .
import heapq
def solution(operations):
    temp, max_ = [], []
    for num in operations:
        heapq.heapify(temp)
        a, b = num.split(' ')
        if a == 'I':
            temp.append(int(b))
        else:
            if len(temp) > 0:
                if b == '1':
                    temp.pop(temp.index(heapq.nlargest(1, temp)[0]))
                else:
                    heapq.heappop(temp)
    if temp:
        return [heapq.nlargest(1, temp)[0], heapq.nsmallest(1, temp)[0]]
    else:
        return [0, 0]


print(solution(operations))
