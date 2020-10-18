T = int(input())
for _ in range(T):
    num = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            # print(arr[i], arr[j])
            if arr[i] > arr[j]:
                count += 1
    print(count)
