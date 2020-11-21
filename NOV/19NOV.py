# 3번의 기회
# 두자리수는 어차피 10 하나
# 1이 나오면 1인지 10인지 확인 => 1 다음이 int형이면 10인거지
def solution(dartResult):
    char_set = ('s', 'd', 't')
    sign_set = ('*','#')
    temp = []
    temp2 = []
    for letter in dartResult:

        try:
            if letter == '0':
                temp.pop()
                temp.append(10) # 이전의 1은 제거해줘야한다.
                continue
            letter = int(letter)
            temp.append(letter)

        except:
            num = temp.pop()
            if letter == "D":
                num = num ** 2
            elif letter == 'S':
                num = num ** 3
            temp.append(num)


    return temp

dartResult = '1D#10S*3S'
print(solution(dartResult))

