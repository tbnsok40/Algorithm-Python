s = '3people unFollowed me'
s = 'for the last week'

def Jaden_Case(s):
    answer =[]
    for i in range(len(s.split())):
        answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:])
    return " ".join(answer)


def solution(s):
    s = s.split(' ')
    temp = []
    answer = ''
    for word in s:
        word = list(word.lower())

        try:
            word[0] = word[0].upper()
        except:
            pass
        temp.append(''.join(word))
    return ' '.join(temp)

print(solution(s))