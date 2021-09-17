from collections import deque


def solution(s1, s2):
    if s1 == s2:
        return 0

    def switch_each(idx_0, idx_adj, answer):
        s1[idx_0], s1[idx_adj] = s1[idx_adj], s1[idx_0]
        answer += 1
        if s1 == s2:
            return answer

    def findAdj(idx_0):
        if idx_0 == 6:
            return [0, 1, 2, 3, 4, 5]
        elif idx_0 == 5:
            return [0, 4, 6]
        elif idx_0 == 0:
            return [1, 5, 6]
        else:
            return [idx_0 - 1, idx_0 + 1, 6]

    answer = 0
    idx_0 = s1.index(0)
    adj_queue = deque(findAdj(idx_0))

    diff_idx = deque()
    for i in adj_queue:
        if s1[i] != s2[i]:
            diff_idx.append(i)
    while diff_idx:
        diff_idx.popleft()


        # for a in zip((s1[i], s2[i])):
        #     print(a)

    # print(s1[adj_queue[0]], s1[adj_queue[1]], s1[adj_queue[2]])
    # visited = [s1]




s1 = [1, 2, 3, 0, 6, 5, 4]
s2 = [1, 2, 3, 4, 5, 6, 0]
print(solution(s1, s2))
