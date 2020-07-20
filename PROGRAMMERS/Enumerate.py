# num, base = map(int, input().strip().split(' '))
num, base = map(int, input().split())
num = list(str(num)) # int형을 하나하나 쪼개어 리스트화 시키는 법
answer = 0
for idx, i in enumerate(num[::-1]):
    answer += int(i) * ( base ** idx )
print(answer)
