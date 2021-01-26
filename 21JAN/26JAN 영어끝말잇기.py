def solution(n, words):
    # 끝말 다르면 break
    # 중복되면 break

    #문제는 어떻게 순서를 계산할 것인지
    idx = 1
    N = len(words)
    answer = [words[0]]

    while idx < N:

        m, r = divmod(idx, n)

        if answer[-1][-1] != words[idx][0]:
            return [r + 1, m + 1]

        if words[idx] not in answer:
            answer.append(words[idx])
        else:
            return [r + 1, m + 1]
        idx += 1
    return [0, 0]

