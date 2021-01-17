def solution(arr, divisor):
    answer = sorted([num for num in arr if num % divisor == 0 ])
    if not answer:
        return [-1]
    return answer