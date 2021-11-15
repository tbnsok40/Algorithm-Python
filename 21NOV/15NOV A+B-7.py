N = int(input())
for i in range(1, N + 1):
    x, y = map(int, input().split(' '))
    print("Case #{0}: {1}".format(i, x+y))
