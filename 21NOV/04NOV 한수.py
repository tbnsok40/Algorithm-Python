N = int(input())  # 1 ~ 1000
count = 0
for i in range(1, N + 1):
    i = str(i)
    if len(i) == 1:
        count += 1

    elif len(i) == 2:
        count += 1

    elif len(i) == 3:
        if (int(i[0]) - int(i[1])) == (int(i[1]) - int(i[2])):
            count += 1
    else:
        break
print(count)
"""
110
"""
