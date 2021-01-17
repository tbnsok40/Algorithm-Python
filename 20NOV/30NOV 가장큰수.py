def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))


numbers = [3,30,34,5,9]
# 제한 사항 중, numbers의 원소는 0이상이라한 점이 함정

print(solution(numbers))