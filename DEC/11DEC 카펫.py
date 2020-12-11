brown = 8
yellow = 1

brown = 24
yellow = 24

def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]
    else:
        temp = list()
        for i in range(1, yellow):
            if yellow % i == 0:
                temp.append((int(yellow / i), i))
        for a, b in temp:
            if brown == ((a + 2) * (b + 2)) - yellow and a >= b:
                return [a+2,b+2]

def solution(brown, yellow):
    total = brown + yellow
    for i in range(1, total + 1):
        if total % i == 0 and yellow == ((int(total / i) - 2) * (i - 2)):
            return [int(total / i), i]
