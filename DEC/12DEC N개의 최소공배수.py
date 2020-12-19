from math import gcd

def lcm(a,b):
    return a*b // gcd(a,b)

def solution(arr):

    while arr:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]

arr = [2,6,8,14]
# arr = [1,2,3]
print(solution(arr))
# 이진 재귀도 고려해볼것



