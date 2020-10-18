from collections import deque
progresses = [93,30,55]
speeds = [1,30,5]
# progresses = [93,30,55]
# speeds = [1,10,8]
def solution(progresses, speeds):
    temp = []
    for i,j in zip(progresses,speeds):
        # print(i,j)
        todo = 100-i
        if (todo/j) != int(todo/j):
            # print(todo/j)
            temp.append(int(todo/j)+1)
        else:
            temp.append(int(todo/j))
    print(temp)
    return make_deque(temp)

def make_deque(temp):
    ans = []
    count = 1
    while True:
        item = temp.pop(0)

        while True:
            item2 = temp.pop(0)
            if item < item2:
                ans.append(count)
                if temp == []:
                break
            else:
                count += 1
            if temp == []:
                ans.append(count)
                break
        if sum(temp) == len(temp):
            break
    return ans
print(solution(progresses,speeds))

