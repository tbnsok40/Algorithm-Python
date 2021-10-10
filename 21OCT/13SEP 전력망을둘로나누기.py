from collections import defaultdict
from itertools import combinations


def dfs(start, wire_dict, visited):
    global count
    count += 1
    visited.append(start)

    for a in wire_dict[start]:
        if a not in visited:
            dfs(a, wire_dict, visited)


def solution(n, wires):
    global count
    result = []
    for wire in combinations(wires, len(wires) - 1):
        wire_dict = defaultdict(list)

        for a, b in wire:
            wire_dict[a].append(b)
            wire_dict[b].append(a)

        count = 0
        dfs(1, wire_dict, [])
        value = abs(n - (count * 2))
        result.append(value)
    return min(result)


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	))
