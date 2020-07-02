# lsi = []
# for _ in range(5):
#     lsi.append(int(input()))

# lis = [u for u in (int(input()) for _ in range(5)) if u >= 40]
# print(lis)

# s = { u for u, v in (input().split() for _ in range(m)) if v == 'W' }

lis = [u if u >= 40 else 40 for u in (int(input()) for _ in range(5))]
print(sum(lis)//5)

