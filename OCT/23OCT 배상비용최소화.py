N = 4
works = [4,3,3]

N = 2
works = [3,3,3]

def solution(N, works):

    while N > 0:
        works.sort()
        if works[-1] == 0:
            return 0
        else:
            works[-1] -= 1
        N -= 1
    works = list(map(lambda x: x**2, works))
    return sum(works)
print(solution(N,works))