a, b = map(int, input().split())
if (a<=b):
    for i in range(1,a+1):
        if ((a/i) == int(a/i)) and ((b/i) == int(b/i)):
            print(i, int(a/i), int(b/i))
else:
    for i in range(1,b+1):
        if ((a/i) == int(a/i)) and ((b/i) == int(b/i)):
            print(i, int(a/i), int(b/i))


# 1위의 코드
apple, banana = map(int, input().split())
for i in range(min(apple, banana)):
    if apple%(i+1)+banana%(i+1)==0:
        print(i+1, apple//(i+1), banana//(i+1))
