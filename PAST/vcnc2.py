n = 5
nationality = [[1,2],[2,3]]
import itertools
from itertools import combinations
def solution(n, nationality):
    temp = set(list(itertools.chain(*nationality)))
    temp2 = []
    for i in range(max(temp) + 1, n + 1):
        temp2.append(i)
    result = set()
    for i in temp:
        temp2.append(i)
        for j in combinations(temp2, 2):

            result.add(j)
            print(result)
        temp2.pop()
    return len(result)

print(solution(n, nationality))