citations = [3,0,6,1,5]
citations = [1,2,3,4,6,7,8,9,10]

# 내가 푼 것
# 잘못 생각한점: citations안의 값만이 h가 될 거라 생각했다. 문제를 반만 이해함 빠끄
def solution(citations):
    citations.sort()
    for idx, i in enumerate(citations):
        if i <= len(citations[idx:]):
            max_h = i
    return max_h

print(solution(citations))
