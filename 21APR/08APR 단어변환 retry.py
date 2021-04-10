answer = 0


def solution(begin, target, words):
    visited = [0] * len(words)
    dfs(begin, target, words, visited)
    return answer


def dfs(begin, target, words, visited):
    stack = []
    global answer
    if begin == target:
        return answer

    if answer > len(words):
        return 0

    # while 0 in visited:
    for i in range(len(words)):
        if sum([1 for a, b in zip(begin, words[i]) if a != b]) == 1 and visited[i] == 0:
            stack.append(words[i])
            print(stack)

            visited[i] = 1
    while stack:
        be = stack.pop()
        answer += 1
        dfs(be, target, words, visited)


begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]



# 이 방법은 되게 느리다 -> 원인이 딕셔너리를 만들어 낸 것 때문인가?
from collections import deque as queue

# 람다를 이렇게 할당하려면 차라리 함수를 쓰지;
# transistable = lambda a, b: sum((1 if x != y else 0) for x, y in zip(a, b)) == 1


def transistable(a, b):
    return sum((1 if x != y else 0) for x, y in zip(a, b)) == 1

def solution(begin, target, words):
    q, d = queue(), dict()
    q.append((begin, 0))
    d[begin] = set(filter(lambda x: transistable(x, begin), words))
    for w in words:
        d[w] = set(filter(lambda x: transistable(x, w), words))
    print(d)
    while q:
        curr, level = q.popleft()
        if level > len(words):
            return 0
        for w in d[curr]:
            if w == target:
                return level + 1
            else:
                q.append((w, level + 1))
    # while문 내에서 return 되지 않으면, 못찾는 걸로 간주하고 0 출력
    return 0


print(solution(begin, target, words))
