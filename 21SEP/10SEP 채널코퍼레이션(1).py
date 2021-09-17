def solution(locations):
    if [2, 2] in locations:
        return -1
    else:
        return len(locations)


# locations = [[1,3], [3,1]]
locations = [[2, 2], [1, 3]]
