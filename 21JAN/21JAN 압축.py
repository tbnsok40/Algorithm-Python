def solution(msg):
    # 딕셔너리 생성하여 c+w를 key로 입력, value는 27~ auto increment
    # 1~26 딕셔너리 사생성
    alpha = {}
    for idx, i in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        alpha[i] = idx + 1

    answer = []
    # 최초 두 글자만 따로 처리하고 그 다음부터 for문
    c = msg[0]
    w = msg[1]
    answer.append(alpha[c])
    answer.append(alpha[w])
    count = 27
    alpha[(c + w)] = count
    msg = msg[2:]

    # 두글자 입력하는 걸로 바꿔야한다.
    for i in range(len(msg)-1):
        cw = msg[i] + msg[i+1]
        if cw in alpha.keys():
            answer.append(alpha[cw])
        else:
            answer.append(alpha[c])
            count += 1
            alpha[cw] = count



    return answer


msg = 'KAKAO'

print(solution(msg))
