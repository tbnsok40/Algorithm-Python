# from itertools import permutations
# for i in list(permutations(items,2)):
#     b.append(i)
# print(b)

# from itertools import combinations
# a = []
# for i in list(combinations(items,2)):
#     a.append(i)
# print(a)


import sys
def read(): return list(map(int, sys.stdin.readline().split()))
items = (read())
# (1,2)(3,4)
# (1,3)(2,4)
# (2,3)(1,4)
def final_min(items):
    min1 = abs((items[0]+items[1]) - (items[3]+items[2]))
    min2 = abs((items[0]+items[2]) - (items[1]+items[3]))
    min3 = abs((items[0]+items[3]) - (items[1]+items[2]))
    final = min(min1,min2,min3)
    return final
print(final_min(items))
# 굳이 list로 묶을 필요가 없었다.

# 다른 사람 풀이
a = list(map(int, input().split()))
a.sort()
print(abs(a[0] + a[3] - a[1] - a[2]))
