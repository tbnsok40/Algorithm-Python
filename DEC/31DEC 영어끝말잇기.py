# (번호, 차례)
# dictionary에 넣으면서 except 발생할 때(2될때) 스탑
# 번호 ==>
# 차례 ==>
# words = ['hello', 'one', 'even','hello', 'never', 'row', 'world', 'traw']
# n = 2

words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
n = 3
# def solution(n, words):
#     word_dict = {}
#     for idx, i in enumerate(words):
#         idx += 1
#
#         try:
#             word_dict[i] += 1
#             return
#         except:
#             word_dict[i] = 1
#
#         if i[-1] != words[idx + 1][0]:
#             return


def solution(n, words):
    before_words = []
    count = 0
    answer = [0, 0]
    for idx, word in enumerate(words):
        count %= n
        if idx >= 1:
            if (word in before_words) | (before_words[-1][-1] != word[0]):
                answer = [count + 1, 1 + idx//n]
                break
        count += 1
        before_words.append(word)
    return answer
# before_words를 없애고, words를 이용해 이전가지 참조하는 방식 채택
# append도 안해도 되고 , 새로운 리스트(before_words)를 안만들어도 된다.
def solution(n, words):
    answer = [0, 0]
    count = 1 # range가 1부터 시작하므로, 1으로 설정
    for idx in range(1, len(words)): # 1부터 시작하는 이유는 첫번째 사람의 첫 단어는 절대 틀릴 일이 없음
        word = words[idx] # words[idx] : 언급된 단어
        count %= n
        if (word in words[0:idx]) or (words[idx-1][-1] != word[0]):
            print(idx, count, word)
            answer = [count + 1, idx//n + 1] # [나머지 + 1, 목 + 1]
            return answer
        count +=1
    return answer
print(solution(n, words))

