import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '123'

for j in itertools.product(iterable1,iterable2,iterable3):
    print(j)

my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])
print(answer)
# 방법2 - list comprehension
answer2 = [element for array in my_list for element in array]
print(answer2)
