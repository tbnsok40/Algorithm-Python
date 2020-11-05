s = 'Z B z'
# 65 ~ 90
# 97 ~ 122
print(ord('~'))

print(chr(65))
print(chr(90))

print(chr(97))
print(chr(122))


n = 4
def solution(s, n):
    answer = ''
    for idx, letter in enumerate(s):
        intLetter = ord(letter)
        if letter != ' ':
            if intLetter <= 90:
                answer += chr(((intLetter + n) % 90) + 65)
            elif intLetter >=97:
                answer += chr(((intLetter + n) % 122) + 97)
        else:
            answer += letter
    print(answer)
    return answer
# 90+25 = 115

print(solution(s,n))