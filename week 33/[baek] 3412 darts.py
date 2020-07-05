import sys
# import math
def read(): return map(int, sys.stdin.readline().split())
# map형식으로 만들었기에 T나 n처럼 하나에만 할당하면 에러가 난다. map 주소를 반환시키기 때문
# T = read()

T = int(sys.stdin.readline())

for _ in range(T):
    sum = 0
    n = int(sys.stdin.readline())
    for _ in range(n):
        x, y = read()
        z = (x**2 + y**2)**(0.5)
        # int를 씌워주면 반올림이 된다. 그러면 범위를 벗어나는 케이스가 생기므로 오답이 발생

        if 0<=z<=20:
            sum += 10
        elif 20< z <= 40:
            sum += 9
        elif 40< z <= 60:
            sum += 8
        elif 60< z <= 80:
            sum += 7
        elif 80< z <= 100:
            sum += 6
        elif 100< z <= 120:
            sum += 5
        elif 120< z <= 140:
            sum += 4
        elif 140< z <= 160:
            sum += 3
        elif 160< z <= 180:
            sum += 2
        elif 180< z <= 200:
            sum += 1
        else:
            sum += 0
    print(sum)
