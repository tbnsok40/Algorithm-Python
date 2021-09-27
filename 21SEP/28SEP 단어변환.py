from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    def checkDiff(alpha, beta):
        diff = 0
        for a, b in zip(alpha, beta):
            if a != b:
                diff += 1
        if diff == 1:
            return True
        else:
            return False

    queue = deque()
    queue.append([begin, 0])
    while queue:
        base_word, count = queue.popleft()
        if base_word == target:
            return count
        for word in words:
            if checkDiff(base_word, word):
                queue.append([word, count + 1])

    return 0


words = ["hot", "dot", "dog", "lot", "log", "cog"]
begin = "hit"
target = "cog"

print(solution(begin, target, words))
