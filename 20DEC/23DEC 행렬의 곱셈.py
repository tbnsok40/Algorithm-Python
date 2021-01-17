arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

# 배운 것: 행렬 전환: zip(*arr)ㅗ

def solution(arr1, arr2):
    ans = []
    for colA in arr1:
        temp = []
        for colB in zip(*arr2):
            sum = 0
            for a, b in zip(colA, colB):
                sum += a * b
            temp.append(sum)
        ans.append(temp)
    return ans

print(solution(arr1, arr2))