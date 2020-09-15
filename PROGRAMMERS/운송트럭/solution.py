def solution(max_weight, specs, names):
    dic = dict()
    for i,j in specs:
        dic[i] = int(j)
    result, count = 0, 1

    for name in names:
        if (result + dic[name]) <= max_weight:
            result += dic[name]
            pass
        else:
            count += 1
            result = 0
            result += dic[name]
    return count

# names = ['toy', 'snack', 'snack']
# specs = [['toy',70], ['snack', 200]]
# max_weight = 300
names = ['toy', 'snack', 'toy']
specs = [['toy','70'], ['snack', '200']]
max_weight = 200

print(solution(max_weight, specs, names))
# for i, j in spec:
#     print(i,j)