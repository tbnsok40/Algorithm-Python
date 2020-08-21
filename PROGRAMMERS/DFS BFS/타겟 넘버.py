numbers = [1,1,1,1,1]
target = 3

### beautiful
from itertools import product
def solution2(numbers, target):
    l = [(x,-x) for x in numbers] # this
    s = list(map(sum, product(*l))) # and this two line is like binary tree maker.
    return s.count(target)
print(solution2(numbers,target))

## DFS
answer = 0
def DFS(idx, numbers, target, curr_value):
    global answer
    if idx == len(numbers) and curr_value == target:
        answer += 1
        return
    if idx == len(numbers):
        return
    DFS(idx+1, numbers, target, curr_value + numbers[0])
    DFS(idx + 1, numbers, target, curr_value - numbers[0])

def solution(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer
print(solution(numbers,target))