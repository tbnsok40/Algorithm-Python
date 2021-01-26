def solution(n,a,b):
    count = 1
    temp = [a, b]
    while n >= 1:
        if abs(temp[0] - temp[1]) == 1 and temp[0]//2 != temp[1]//2:
            return count
        n /= 2
        count += 1
        for i in range(2):
            temp[i] /=  2
            if temp[i] != int(temp[i]):
                temp[i] = int(temp[i]) + 1

print(solution(8, 4, 7))

def solution(n,a,b):
    count = 1
    while n >= 1:
        if abs(a - b) == 1 and a//2 != b//2:
            return count
        a /=  2
        if a != int(a):
            a = int(a) + 1
        b /= 2
        if b != int(b):
            b = int(b) + 1
        n /= 2
        count += 1
