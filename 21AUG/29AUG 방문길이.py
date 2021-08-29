def solution(dirs):
    result = [0, 0]
    route = {}
    dir_dict = {
        "U": [0, 1],
        "D": [0, -1],
        "L": [-1, 0],
        "R": [1, 0],
    }

    for dir in dirs:
        if (-5 <= result[0] + dir_dict[dir][0] <= 5) and (-5 <= result[1] + dir_dict[dir][1] <= 5):
            a = result[0] + dir_dict[dir][0]
            b = result[1] + dir_dict[dir][1]

            route[str(result[0]) + str(result[1]) + str(a) + str(b)] = 1
            route[str(a) + str(b) + str(result[0]) + str(result[1])] = 1

            result[0] = a
            result[1] = b

    return len(route) // 2
