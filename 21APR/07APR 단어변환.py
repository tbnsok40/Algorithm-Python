# 정답 코드
# def solution(begin, target, words):
#     answer = 0
#     queue = [begin]
#
#     while True:
#         tmp_q = []
#         for word1 in queue:
#             if word1 == target:
#                 return answer
#
#             for word2_idx in range(len(words)-1, -1, -1):
#                 word2 = words[word2_idx]
#                 difference = sum([x != y for x, y in zip(word1, word2)])
#                 if difference == 1:
#                     tmp_q.append(words.pop(word2_idx))
#         if not tmp_q:
#             return 0
#         queue = tmp_q
#         answer += 1
# pop 해주는 것이 결국 visited를 체크하는 것 -> 근데 pop보단 visited 체크가 더 안전하지 않을까 싶기도함. (괜히 원본 리스트 건드는 것 보다야..)

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]

# 오답 코드
# def solution(begin, target, words):
#     queue = [begin]
#     answer = 0
#     while queue:
#         curr = queue.pop()
#         if curr == target:
#             return answer
#
#         for i in range(len(words) - 1, -1, -1):
#             temp = [1 for a, b in zip(curr, words[i]) if a != b]
#             if sum(temp) == 1:
#                 queue.append(words.pop(i))
#
#         # queue를 업데이트 해줘야하는게, 선택단어마다 연관된 단어 queue가 매번 달라질 것임
#         # 그렇기 때문에 각 연관단어를 담을 temp_q를 만들어 iter마다 초기화 해줘야한다. => 난 그 초기화 작업이 없다.
#         answer += 1
#
#     if not words:
#         return 0