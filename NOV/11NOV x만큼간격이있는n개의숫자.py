def solution(x, n):
    answer = []
    # 예외 처리해줘야 하는 곳. x는 정수라 했으니, 양수/음수 뿐만 아니라 0일 때도 고려해줘야한다.
    if x == 0:
        return [0]*n
    for i in range(x, x*(n+1), x):
        answer.append(i)
    return answer
