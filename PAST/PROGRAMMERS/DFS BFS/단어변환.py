from collections import deque as queue

trans = lambda a,b: sum((1 if x != y else 0) for x,y in zip(a,b)) == 1
begin = 'hit'
target = 'cog'
words =['hot', 'dot', 'dog', 'lot','log', 'cog']

def solution3(begin, target,words):
    q,d = queue(), dict()
    # 최초 큐 삽입
    q.append((begin,0))

    # dictionary 완성
    d[begin] = set(filter(lambda word: trans(word,begin),words))
    for word1 in words:
        d[word1] = set(filter(lambda word: trans(word,word1),words))

    # 큐 반복
    while q:
        node, level = q.popleft()

        if level > len(words):
            return 0

        for word in d[node]:
            if word == target:
                return level + 1
            else:
                q.append((word, level+1))
    return
print(solution3(begin,target,words))




# 각 단어별, transible 한 단어들을 딕셔너리 형태로 만든다.
# 어떤 단어를 탐색하고 싶으면, 해당 key를 for문으로 queue에 삽입
# queue에서 pop하는 형태로 한다.
# pop 된 것이 target과 맞으면 level+1해서 return
# 그 외는 level+1해서  queue에 append