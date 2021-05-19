left = 13
right = 17


def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if get(num) == "+":
            answer += num
        else:
            answer -= num
    return answer


def get(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count % 2 == 0:
        result = "+"
    else:
        result = "-"
    return result


# refactoring 할 것
print(solution(left, right))
