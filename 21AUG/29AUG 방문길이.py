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
            new_x = result[0] + dir_dict[dir][0]
            new_y = result[1] + dir_dict[dir][1]

            route[str(result[0]) + str(result[1]) + str(new_x) + str(new_y)] = 1
            route[str(new_x) + str(new_y) + str(result[0]) + str(result[1])] = 1

            result[0] = new_x
            result[1] = new_y

    return len(route) // 2
