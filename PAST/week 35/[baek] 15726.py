a, b, c = map(int, input().split())
if int(a*b/c) > int(a/b*c):
    print(int(a*b/c))
else:
    print(int(a/b*c))
