Num = int(input())
lists = list(map(int, input().split()))
for i in range(len(lists)):
    if lists[i] == -1:
        index = i
left = min(lists[:index])
right = min(lists[index+1:])
print(left+right)