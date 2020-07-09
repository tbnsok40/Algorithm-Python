import sys
def read(): return sys.stdin.readline()
seconds = int(read())
# print(seconds)
one = [0,0]
sign = True
move = 1
while True:
    if sign:
        for i in range(move):
            one[1]+=1
            seconds -= 1
            if seconds == 0:
                print(*one)
                sys.exit()

        for j in range(move):
            one[0] += 1
            seconds -= 1
            if seconds == 0:
                print(*one)
                sys.exit()

    else:
        for i in range(move):
            one[1] -= 1
            seconds -= 1
            if seconds == 0:
                print(*one)
                sys.exit()
        for j in range(move):
            one[0] -= 1
            seconds -= 1
            if seconds == 0:
                print(*one)
                sys.exit()

    sign = not sign
    move += 1
