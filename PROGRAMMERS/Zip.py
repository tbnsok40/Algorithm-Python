# list1.sort() # deepcopy, 원본을 바꿔버린다
# sorted(list1) # 원본을 바꾸지 않고 출력할 수 있다.
list2 = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*list2)))
print(*list2)

# 1
mylist = [ 1,2,3 ]
new_list = [ 40, 50, 60 ]
for j in zip(mylist, new_list):
   print(j)

# 2
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for i,j,k in zip(list1, list2, list3):
   print( i,j,k)

# 3 딕셔너리 만들기
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds))
print(answer)