N = 4
works = [4,3,3]
# works = [5,3,2,4,6]
# while 문을 N번 돌린다.
# N번씩, 가장 큰 원소를 하나씩 차감
# while문이 끝난 후 works 리스트 계산
# 최대힙 만들어서, 루트를 -1씩


import heapq
def solution(N, works):
    while N>0:
        works.sort()
        if works[-1] == 0:
            break
        works[-1] -= 1
        N -= 1 # 굳이 while을 안쓰고 for를 써도 되는 부분
    ##########################
    for i in range(N):
        works.sort()
        works[-1] -= 1
    ###########################

    after = list(map(lambda  x: x**2, works))
    return sum(after)
# 18, 19 줄은 아래처럼 줄일 수 있다.
    return sum([i**2 for i in works])
print(solution(N, works))


# Tim sort
def solution(no, works):
    if no >= sum(works):
        return 0
    for _ in range(no):
        works = sorted(works)
        works[-1] -= 1
    return sum([work ** 2 for work in works])
