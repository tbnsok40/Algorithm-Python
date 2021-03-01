land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i -1][: j] + land[i - 1][j + 1:])
    return max(land[-1])
print(solution(land))

# land[i -1][: j] + land[i - 1][j + 1:] <= 이건 어떠한 값이 아니라, 하나의 합쳐진 리스트가 된다.
# [12] + [11, 10] => [12, 11, 10]