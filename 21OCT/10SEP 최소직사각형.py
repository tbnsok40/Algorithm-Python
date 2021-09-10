def solution(sizes):
    for size in sizes:
        size.sort()
    max_x = -1
    max_y = -1
    for x, y in sizes:
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y
    return max_y * max_x

print(solution(sizes=[[60, 50], [30, 70], [60, 30], [80, 40]]))

