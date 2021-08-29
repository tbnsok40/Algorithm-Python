
def calculate(num_bin, new_bin):
    count = 0
    for a, b in zip(num_bin, new_bin):
        if a != b:
            count += 1
    if count <= 2:
        return True
    else:
        False


def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = bin(num)[2:]
        while True:
            num += 1
            bin_new = bin(num)[2:]
            diff = len(bin_new) - len(bin_num)
            if diff > 0:

                if calculate('0' * diff + bin_num, bin_new):
                    answer.append(num)
                    break
            else:
                if calculate(bin_num, bin_new):
                    answer.append(num)
                    break

    return answer


numbers = [2, 7]

print(solution(numbers))
