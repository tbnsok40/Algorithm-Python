# (번호, 차례)
# dictionary에 넣으면서 except 발생할 때(2될때) 스탑
# 번호 ==>
# 차례 ==>
words = ['hello', 'one', 'even','hello', 'never', 'row', 'world', 'traw']
n = 2

# words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
# n = 3
def solution(n, words):
    word_dict = {}
    for idx, i in enumerate(words):
        idx += 1

        try:
            word_dict[i] += 1
            return
        except:
            word_dict[i] = 1

        if i[-1] != words[idx + 1][0]:
            return

print(solution(n, words))