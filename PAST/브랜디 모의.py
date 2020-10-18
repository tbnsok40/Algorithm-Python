N,k = input().split()
a = input().split()
N = len(a)
mini = min(a)
min_index = a.index(mini)
k = 4
for i in range(k):
    left = a[:min_index-i]
    right = a[min_index-i:]
    if len(left)%k == 1 and len(right)%k == 1:
        print((N)//(k-1))
    print((N) // (k - 1))
# while min_index+4< len(a)+4:
#     print(a[min_index-1:(min_index-1) + 4])
#     min_index = min_index+3
#     count += 1

# 31 36 20 30 1 9 6 13 3 29 11 25 7 8 2 24 34 18 26 15 23 28 37 19 21 4 32 14 16 10 12 27 22 35 5 17 33

# 7 3 1 8 4 6 2 5