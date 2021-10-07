from itertools import combinations


def solution(n, wires):
    answer = float('inf')

    if n == 2:
        # print('thi')
        return 0
    new_wires = []
    for wire in wires:
        new_wires.append(sorted(wire))

    for case in combinations(new_wires, n - 2):
        case = sorted([*case])
        # case.sort()
        first = []

        for nodes in case:
            if not first:
                first += nodes

            a, b = nodes
            if a in first or b in first:
                first += sorted(nodes)
        absolute_value = abs(len(set(first)) - (n - len(set(first))))

        # print(case)
        # print(first, len(set(first)) , (n - len(set(first))))
        # print(' ')
        answer = min(answer, absolute_value)
    return answer


# 하나씩 돌려가며 제거하든, 제외하여 연산한다.
# first 만 구하면 second 는 자연스레 구해진다.


# n = 9
# wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 7], [4, 6], [7, 8], [7, 9]]

# n = 7
# wires = [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]
n = 6
wires = [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]]
answer = 2

print(solution(n, wires))
