# 에러 존재
li = [3,30,34,9,100,200,1000]
# 정렬
# 십의 단위로 indexing
# def solution(li):
#     one = []
#     dec = []
#     hund = []
#     thou = []
#     li.sort()
#     for idx, i in enumerate(li):
#         if (i) < 10:
#             one.append(str(i))
#         elif (10<=i)and(i<100):
#             dec.append(str(i))
#         elif (100<=i) and (i<1000):
#             hund.append(str(i))
#         else:
#             thou.append(str(i))
#     return ('').join(one[::-1]) + ('').join(dec[::-1])+ ('').join(hund[::-1])+('').join(thou[::-1])

li = [3, 330, 34, 5, 9,1000]

def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers)
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))
# 지린다
print(solution(li))