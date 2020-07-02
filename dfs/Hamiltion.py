gra = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
       [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 1
       [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],  # 2
       [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],  # 3
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 4
       [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],  # 5
       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],  # 6
       [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # 7
       [0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],  # 8
       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],  # 9
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],  # 10
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],  # 11
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]  # 12
n = 12
vIndex = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def hamilton(i):
    j = 1
    if promising(i):
        if i == (n - 1):
            for j in range(n):
                print(j, vIndex[j])
            print()
        else:
            for j in range(2, n + 1):
                vIndex[i + 1] = j
                hamilton(i + 1)


def promising(i):
    if i == n - 1 & (gra[vIndex[n - 1]][vIndex[0]] == 0):
        bSwith = 0
    elif (i > 0) & (gra[vIndex[i - 1]][vIndex[i]] == 0):
        bSwith = 0
    else:
        bSwith = 1
        j = 1
        while j < i & bSwith:
            if vIndex[i] == vIndex[j]:
                bSwith == 0
            j += 1
    return bSwith


print(hamilton(1))
