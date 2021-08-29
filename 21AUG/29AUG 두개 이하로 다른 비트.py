def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'

        if number % 2 == 1:
            bin_number[idx + 1] = '0'
        answer.append(int(''.join(bin_number), 2))

    return answer


numbers = [2, 7]

print(solution(numbers))
# 순회하지 말고 조작하라

