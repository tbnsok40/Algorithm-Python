# 3번의 기회
# 두자리수는 어차피 10 하나
# 1이 나오면 1인지 10인지 확인 => 1 다음이 int형이면 10인거지
def solution(dartResult):
    temp = []
    for letter in dartResult:

        try:
            if letter == '0' and temp[-1] == 1:
                temp.pop()
                temp.append(10) # 이전의 1은 제거해줘야한다.
                continue
            elif letter == '0' and temp[-1] != 1:
                pass
            letter = int(letter)
            temp.append(letter)

        except:
            num = temp.pop()
            if letter == "D":
                num = num ** 2
                temp.append(num)
            elif letter == 'T':
                num = num ** 3
                temp.append(num)
            elif letter == 'S':
                temp.append(num)

            try:
                if letter == '*' and temp:
                    num = num * 2
                    num2 = temp.pop() * 2
                    temp.append(num2)
                    temp.append(num)
                elif letter == '*' and not temp:
                    num = num * 2
                    temp.append(num)
                elif letter == '#':
                    num = num * (-1)
                    temp.append(num)
            except IndexError:
                pass
    return sum(temp)

dartResult = '1D#2S*3S'
# dartResult = '1S*2T*3S'
dartResult = '1D2S0T'
print(solution(dartResult))
