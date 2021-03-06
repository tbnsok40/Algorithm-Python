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


# 다른 사람 풀이, 굳이 n을 쓸 필요가 없었다
def solution(n,a,b):
	answer = 0
	while a != b:
		answer += 1
        # 1을 더해서 2로 나누었을 때, 자리수를 맞춰줌
        # 예) 1, 2의 경우는 2, 3으로 해서 나눴을때 몫이 1이 되도록
		a, b = (a+1)//2, (b+1)//2
	return answer