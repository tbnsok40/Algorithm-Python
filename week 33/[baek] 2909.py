import sys
def read(): return map(int, sys.stdin.readline().split())
c,k = read()

# c = str(c)
# if int(c[-k]) < 5:
#     result = c[:-k] + '0'*k
# else:
#     result = c[:-k] + '0'*k
#     result = int(result) + 10**k
# print(int(result))

################################

c, k = read()
if k == 0:
    print(c)
else:
    t = 10 ** k # t: 10단위
    n = c // t * t # 해당 단위 밑으로는 반올림(내림)

    a = len(str(c)) - k # 전체 자릿수 - k

    if int(str(c)[a]) < 5:
        print(n)
    else:
        print(n + t)


# 어느 반례를 못뚫었는지
# 만약 액면가가 1원이면?
