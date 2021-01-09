n = 6
cars = [6, 4, 10, 9, 8, 4]
links = [[4, 1], [3, 2], [1, 6], [5, 3], [1,5]]

# [[1, 4], [1, 6], [1, 5], [2, 3], [3, 5]]






# 입력 순서에 따라 중복됨을 확인 못할 수 있기에 좋은 방법 아니다.
def solution(n, cars, links):
    chains = len(links)
    links = sorted([sorted(i) for i in links])
    temp = []
    temp += links[0]
    result = []
    for i in range(chains):
        links_copy = links[:]
        del links_copy[i]
        result.append(links_copy)
    answer = []
    temp = []

    for temp in result:
        A, B = [], []
        for idx, i in temp:
            if i[0] == temp[idx + 1][0] or i[1] == temp[idx + 1][1]:
                A += i

                if idx == len(temp) - 1:
                    A += temp[idx + 1]
                    break

            else:
                B += i
                if idx == len(temp) - 2:
                    B += temp[idx + 1]
                    break

        print(i)

    return

print(solution(n, cars, links))

