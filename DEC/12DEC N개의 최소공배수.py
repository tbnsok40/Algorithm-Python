from math import gcd
import heapq

def solution(arr):
    total = 1
    heap = []
    for k in arr:
        total *= k
        heapq.heappush(heap,(-k, k))
    while heap:
        i, j = heapq.heappop(heap), heapq.heappop(heap)
        i, j = i[1], j[1]
        temp = gcd(i, j)
        print(i, j, temp)
        if len(heap) == 0:
            break
        heapq.heappush(heap, (-temp, temp))
        # print('rest+heap: ', heap)
    print()
    return total // temp

arr = [2,6,8,14]
# arr = [1,2,3]
print(solution(arr))
# 이진 재귀도 고려해볼것



print(7*14 // gcd(14,7))