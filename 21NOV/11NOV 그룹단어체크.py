N = int(input())
count = 0
for _ in range(N):
    string = list(input())
    visited = [string[0]]

    for idx in range(len(string) - 1):
        if string[idx] != string[idx + 1]:
            if string[idx + 1] not in visited:
                visited.append(string[idx + 1])
            else:
                break
    else:
        count += 1

print(count)

"""
aba x
aab o
ccde o
cdec x

ffgaf x
앞에서부터 비교(바로 뒤와)
일단 visited 에 넣는다.
달라지면 또 visited 에 넣는다. 달라진 원소를
하다가 또 달라지면 visited에 넣는대, 이미 visited에 있으면 break


"""
