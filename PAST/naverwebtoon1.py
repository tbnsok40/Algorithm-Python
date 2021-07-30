def solution(numbers):
    answer = []
    result = []

    number_hash = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    for i in numbers:
        temp = ''
        for j in str(i):
            temp += number_hash[j]
        answer.append((temp, i))

    answer.sort()
    for i in answer:
        result.append(i[1])
    return result


numbers = [4, 5, 11]


print(solution(numbers))
