begin = 'hit'
target = 'cog'
words =['hot', 'dot', 'dog', 'lot','log', 'cog']
# a = begin
# for b in words:
#     transistable = lambda a, b: sum((1 if x!=y else 0) for x,y in zip(a,b)) == 1
# print((transistable))

from collections import deque as queue

transistable = lambda a, b: sum((1 if x != y else 0) for x, y in zip(a, b)) == 1


def solution(begin, target, words):
    q, d = queue(), dict()
    q.append((begin, 0))
    d[begin] = set(filter(lambda x: transistable(x, begin), words))
    print(d)
    for w in words:
        d[w] = set(filter(lambda x: transistable(x, w), words))
    print(d)
    while q:
        cur, level = q.popleft()
        if level > len(words):
            return 0
        for w in d[cur]:
            if w == target:
                return level + 1
            else:
                q.append((w, level + 1))

    return 0

print(solution(begin,target,words))