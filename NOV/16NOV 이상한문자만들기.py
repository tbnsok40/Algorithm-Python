s = ' try   hello world'
s = ' print hello   world'
s = '    print   h e l l o   wor  ld'
# s = 'AAAAaAA   nnAAAAA     A A A A AAAAA AAA'
# 공백이 연속됨을 고려못한 풀이
def solution(s):
    s = s.lower()
    words = s.split(' ')
    answer = ''
    for word in words:
        for idx, letter in enumerate(word):
            if idx % 2 == 0:
                answer += letter.upper()
            else:
                answer += letter
        answer += ' '
    return answer
# 연속된 공백 처리 ok but 끝에 rstrip(' ')해줘야 하는 상황을 만들어 놓은게 에러 원인
print(solution(s))

# 남의 풀이
def solution(s):
    charlist = ""
    idx = 0
    for i in s:
        if i.isalpha():
            idx += 1
            if idx % 2 != 0:
                charlist += i.upper()
            else :
                charlist += i.lower()
        else:
            idx = 0
            charlist += ' '
    return charlist
print(solution(s))


# 한줄 샷
def solution(s):

    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split(' ')])

print(solution(s))

# 아 공백이 들어오면 공백대로 입력을 해야한다 => 공백이 3칸이면 공백 3개 넣어주깅
