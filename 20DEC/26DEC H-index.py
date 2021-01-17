citations = [3,0,6,1,5]
citations = [0,1]

# 내가 푼 것
# 잘못 생각한점: citations안의 값만이 h가 될 거라 생각했다. 문제를 반만 이해함 빠끄
# def solution(citations):
#     citations.sort()
#     for idx, i in enumerate(citations):
#         if i <= len(citations[idx:]):
#             max_h = i
#     return max_h


# 정답
def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l - i:
            return l - i
    return 0 # 여긴 왜 0이 들어가야한지?

print(solution(citations))
