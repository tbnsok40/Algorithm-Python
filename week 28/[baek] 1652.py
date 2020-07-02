N = int(input())
bed_h = 0
bed_v = 0

temp = []
for i in range(N):
    m = (input())
    temp.append(m)

for row in temp:
    count = 0
    tmp = 0
    for i in row:
        if (tmp == i)&(i == '.')&(count<1) :
            count += 1
            bed_h +=1
        if i == '.':
            tmp = i
        else:
            tmp = 'X'
            count = 0
        # print(row, i, tmp, bed_h)



temp = list(zip(*temp))
# tmp = 0
# print('vertical')
for row in temp:
    count = 0
    tmp = 0
    for i in row:
        if (tmp == i)&(i == '.')&(count<1) :
            count += 1
            bed_v +=1
        if i == '.':
            tmp = i
        else:
            tmp = 'X'
            count = 0
        # print(row, i, tmp, bed_v)
print(bed_h,bed_v)