numbers = map(int, input().split())
numbers  = list(numbers)
# print(numbers)
from math import gcd
def lcm(x,y):
    return x*y // gcd(x,y)
min = 10000000
# numbers = [30,70,35,90,42]
for i in range(len(numbers)-2):
    for j in range(i+1,len(numbers)-1):
        for k in range(j+1,len(numbers)):
            num = lcm(lcm(numbers[i],numbers[j]),numbers[k])
            if num < min:
                min=num
print(min)


# def gcd(x,y):
#     while y:
#         x, y = y, x%y
#     return x
