from itertools import permutations
# from itertools import combinations

numbers = '17'
numbers = '011'

def solution(numbers):
    result = 0
    list1 = [] # 이렇게 리스트 선언하는 것 보다 (2038)
    list1 = list() # 이렇게 선언하는게 더 빨라 (1918)
    numbers = list(numbers)
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            list1.append(('').join(j))
    result += sosu(list1)
    return result

def sosu(list1):
    list1 = set((map(int ,list1)))
    count = 0
    for num in list1:
        if num > 1:
            for k in range(2,num):
                if (num % k) == 0:
                    break
            else:
                count += 1
    return count
# 이중 for문을 2개나 썼다, 안예뻐
print(solution(numbers))
