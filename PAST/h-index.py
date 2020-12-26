
citations = [3,0,6,1,5]

citations = [1,2,8,4,6,5,0,12,34,23,4]
def solution(citations):
    citations.sort()
    l = len(citations)
    print(citations)
    for i in range(l):
        if citations[i] >= l-i:
            print(citations[i], i, l)
            # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return l-i
    return 0
# def solution(citations):
#     citations.sort()
#     print(citations, len(citations))
#     if sum(citations) // len(citations) == citations[0]:
#         return 0
#
#     for idx, i in enumerate(citations):
#         if i <= len(citations[idx:]):
#             print(i, len(citations[idx:]))
#             max_h = i
#             print(max_h)
#     return max_h

print(solution(citations))

# 1. h번 이상 인용횟수 논문이 h편 이상
# 2. 나머지 논문이 h번 이하 인용됐다면
# 3. h 최댓값이 h-index

#1. sorting
#2.