
def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr
arr = [4,3,2,1,5]
print(solution(arr))