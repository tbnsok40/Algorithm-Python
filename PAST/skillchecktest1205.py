def solution(number, k):
    temp = sorted(number)[:k]

    number_copy = number
    print(temp, number, number_copy)
    number = list(number)
    for idx, i in enumerate(number_copy):
        if i in temp:
            temp.remove(i)
            number.remove(i)


    return ''.join(number)


number = "1231234"
k = 3
print(solution(number, k))