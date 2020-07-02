# N = 1 일 때 케이스 생각해주어야 한다.
# 자체루프가 생기는 경우를 생각해주어야 해
test = int(input())
for _ in range(test):
    N = int(input())
    arr = [0]
    for _ in range(N):
        arr.append(int(input()))
    # print(arr)
    cnt = 0
    i = 0
    if N == 1:
        print(1)
        exit()

    while cnt <= (N+1):

        cnt += 1
        if arr[i] == N:
            print(i)
            break
        i += 1
    print(i)
    print(cnt)
    print(0)