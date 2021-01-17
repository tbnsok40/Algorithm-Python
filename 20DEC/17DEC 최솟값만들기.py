def solution(A,B):
    A_srt = sorted(A)
    B_srt = sorted(B, reverse=True)

    answer = 0
    for a, b in zip(A_srt, B_srt):
        answer += a*b
    return answer