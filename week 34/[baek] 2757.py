inputs = input()
inputs =inputs.strip('R') # 중간letter는 왜 strip안돼?
inputs = inputs.replace('C',',')
inputs = list(inputs.split(','))
print(inputs[0], inputs[1])

# strip은 끝단의 공백이나 문자만 제거할 수 있다.

# inputs[1]이 문제
# inputs[0]는 그대로 출력하면 돼
# 26단위마다 Z찍고, 새로운 자릿수 생성

# A~Z (26)
# AA ~ AZ(52), BA ~ BZ(53~78), CA ~ CZ, ... YA ~ YZ, ZA ~ ZZ (26 + 26* 26)
# AAA ~ ZZZ ( 26*1 + 26*2 + 26*3)
# 26*(1 + 26 + 26**2)
# 알파벳이 세자리면 위의 식처럼 항이 세개 생긴다
sum = 26
for j in range(2,8):
    if (int(inputs[1]) // sum) < 1:
        print('자리:',j-1)
        mid = int(inputs[1]) - temp
        print(mid)
        print(mid//26,'번째', mid%26)
        print((mid//26)//26)

        break
    else:
        temp = sum
        sum += 26**j



