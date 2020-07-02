zero = [0]
lis = []

N = int(input())
for _ in range(N):
    lis.append(int(input()))
lis = sorted(lis, reverse=True)
lis = zero + lis
# print(lis)
sum = 0
for j in range(1, len(lis)):
    result =  lis[j] - (j-1)
    if result < 0:
        result = 0
    # print('result',result)
    sum += result
    # print('sum',sum)
print(sum)


