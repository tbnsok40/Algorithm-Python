s = '3people unFollowed me'
s = 'for the last week'
def solution(s):
    s = s.split(' ')
    temp = []
    for word in s:
        word = word.lower()
        word = list(word)
        try:
            word[0] = word[0].upper()
        except:
            pass
        temp.append(''.join(word))
    return ' '.join(temp)

print(solution(s))

li = 'abc'
print(li.upper())