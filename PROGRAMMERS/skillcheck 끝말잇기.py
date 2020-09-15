def solution(n, words):
    word_dict = dict()
    for idx, word in enumerate(words):
        try:
            word_dict[word] += 1
            save_idx = idx + 1
            print('break point', idx)
            break
        except:
            word_dict[word] = 1
    # print(word_dict)

    
    #9
    if (save_idx % n) == 0:
        no_person = n
    else:
        no_person = (save_idx % n)
    print(save_idx)
    if (save_idx / n) <= n:
        no_game = n



    return [no_person,no_game]

words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'nother', 'robot', 'tank','kor']
# words =['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
n = 3
print(solution(n,words))