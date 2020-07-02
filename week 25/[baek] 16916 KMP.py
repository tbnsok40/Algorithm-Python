# 시간 초과
s = input()
p = input()
last = len(p) - 1
for a in range(len(s)-last):
    ans = ''
    if (s[a] == p[0]) & (s[a+last] == p[last]):
        if s[a:a+last+1] == p:
            print(1)
            break
    if a == len(s)-last-1:
        if ans == '':
            print(0)

if p in s:
    print(1)
else:
    print(0)

s = input()
p = input()
print((p in s))