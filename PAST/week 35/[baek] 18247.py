T = int(input())
# L은 12번째 행, 찾고자 하는 것은 12행 4열
# 11행까지 몇의 숫자로 채워지는지, 그리고 + 4 하면 돼.
for _ in range(T):
    a, b = map(int, input().split())
    if (a >= 12) and (b>=4):
        result = 11*b + 4
    else:
        result = -1

    print(result)

