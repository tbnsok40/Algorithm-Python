import sys

def read(): return sys.stdin.readline().strip()

word1 = read()
while True:
    if (len(word1) == 3):
        temp = word1[-1]
        break
    else:
        continue

count = 0
while count < 3:
    word2 = read()
    if (len(word2) == 3) and (temp == word2[0]):
        print('정답입니다.')
        print('게임 끝')
        sys.exit()
    else:
        print('다시 입력하세요')
        count +=1
        continue
print('Game over')