import sys
def read(): return sys.stdin.readline().strip('\n')
n,m = map(int, input().split())
left = list(read())
right = list(read())
left.reverse()
t = int(input())

total = left+right

total_dic = dict()
total_dic[0] = left
total_dic[1] = right

while t > 0 :
    i = 0
    while i < (len(total)-1):
        if total[i] in total_dic[0]:
            if total[i+1] in total_dic[1]:
                total[i], total[i+1] = total[i+1], total[i]
                i += 1
        i +=1
    t -= 1
# print(total)
for i in range(len(total)):
    print(total[i],end='')