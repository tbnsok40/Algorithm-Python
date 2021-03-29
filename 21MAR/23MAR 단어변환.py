def solution(begin, target, words):
    answer = 0
    queue = [begin]
    while True: # 리턴 나오기 전까지 무한 반복
        tmp_q = []
        for word_1 in queue:
            if word_1 == target:
                return answer

            for word_2_idx in range(len(words)-1, -1, -1): # 비교해야할 단어의 인데스를 리턴 -> indexError 방지위해
                word_2 = words[word_2_idx]
                difference = sum([x != y for x, y in zip(word_1, word_2)])
                if difference == 1:
                    pops = words.pop(word_2_idx)
                    print(word_2_idx, pops)
                    tmp_q.append(pops) # tmp_q 에 넣으면 변환가능한 단어 후보인 것 => 얘네를 기준으로 이제 뿌리를 내려간다.
        if not tmp_q:
            return 0
        queue = tmp_q # 이제 queue 를 tmp_q 로 대체한다 (왜냐면 얘한테 변환가능한 후보들이 있으니까)
        answer += 1


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))


def solution2(begin, target, words):
    answer = 0
    queue = [begin]
    while True:
        tmp_q = []
        for word1 in queue:
            if word1 == target:
                return answer
            for word2_idx in range(len(words)-1, -1, -1):
                word2 = words[word2_idx]
                difference = sum([x != y for x, y in zip(word1, word2)])
                if difference == 1:
                    tmp_q.append(word2) # pop()으로 없애 주지 않으면 타임아웃 된다.
        if not tmp_q:
            return 0
        queue = tmp_q
        answer += 1
print(solution2(begin, target, words))





