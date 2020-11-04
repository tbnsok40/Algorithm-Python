def solution(numbers):
    answer = list()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append((numbers[i] + numbers[j]))
    # sort를 먼저하느냐 나중에 하느냐에서 4,5번이 갈린다.
    # why???
    answer = list(set(answer))
    answer.sort()
    return answer