# map(functions_to_apply, list_of_inputs)
# 첫번째 인자에 functions_to_apply -> 자료형이 들어간다면, 해당 자료형으로 바꿔준다는 함수로 생각하자

1
list1 = ['1', '100', '33']
print(list(map(int, list1)))

items = [1,2,3,4]
squared = map(lambda x: x**2, items)
print(squared) # 이대로 프린트하면 map object형태로 출력된다.

def solution(mylist):
    return list(map(lambda x: x**2, mylist)) # list()를 씌워주도록 하자
print(solution(squared))

2
list2 = [[1,2],[3,4],[5]]
def solution(mylist):
    return list(map(list.__len__, mylist))
print(solution(list2))
