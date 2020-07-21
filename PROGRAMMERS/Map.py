1
list1 = ['1', '100', '33']
print(list(map(int, list1)))

2
list2 = [[1,2],[3,4],[5]]
def solution(mylist):
    answer = list(map(list.__len__, mylist))
    return answer
print(solution(list2))
