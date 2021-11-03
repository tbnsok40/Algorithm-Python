import sys

N = int(sys.stdin.readline().rstrip())
numbers = []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        numbers.append(num)
    else:
        numbers.pop()

print(sum(numbers))


"""
10
1
3
5
4
0
0
7
0
0
6

NO 조건
앞뒤로 1 차이일 때, 앞 보다 이전의 수가 앞보다 크면 안된다.
"""
