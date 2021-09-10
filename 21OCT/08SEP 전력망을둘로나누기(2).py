from itertools import combinations
from collections import defaultdict, deque


def solution(n, wires):
    for combi in combinations(wires, len(wires) - 1):

        # dictionary 사용 못하겠다
        # wire_dict = defaultdict(list)
        # for k, v in combi:
        #     wire_dict[k].append(v)

    return answer




# n = 9
# wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 7], [4, 6], [7, 8], [7, 9]]

# n = 7
# wires = [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]
n = 6
wires = [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]]
answer = 2

print(solution(n, wires))
