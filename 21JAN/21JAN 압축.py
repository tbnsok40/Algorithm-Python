# def solution(msg):
#     # 딕셔너리 생성하여 c+w를 key로 입력, value는 27~ auto increment
#     # 1~26 딕셔너리 사생성
#     alpha = {}
#     for idx, i in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
#         alpha[i] = idx + 1
#
#     answer = []
#
#     for i in range(len(msg) - 1):
#
#


    # 최초 두 글자만 따로 처리하고 그 다음부터 for문
    # c = msg[0]
    # w = msg[1]
    # answer.append(alpha[c])
    # answer.append(alpha[w])
    # count = 27
    # alpha[(c + w)] = count
    # msg = msg[2:]
    #
    # # 두글자 입력하는 걸로 바꿔야한다.
    # for i in range(len(msg)-1):
    #     cw = msg[i] + msg[i+1]
    #
    #     # 두글자가 딕셔너리에 있을 때, answer에 value넣어주고, 두글자 + 뒤에글자도 추가해줘야함
    #     if cw in alpha.keys():
    #         answer.append(alpha[cw])
    #         try:
    #             temp = cw + msg[i+2]
    #             count += 1
    #             alpha[temp] = count
    #         except:
    #             pass
    #
    #     else:
    #         answer.append(alpha[c])
    #         count += 1
    #         alpha[cw] = count
    #     print(i, cw, answer)


    # return answer


msg = 'ABABABABABABABAB'
def solution(msg):
    table = dict()
    for idx, value in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ",1):
        table[value] = idx
        last_idx = idx
    idx = 1
    answer = []
    letter = msg[0]
    while idx < len(msg):
        # 현재 입력 + 다음 글자 조합이 색인에 없는 경우
        if letter + msg[idx] not in table:
            # 현재 입력을 answer 배열에 저장
            answer.append(table[letter])
            # 새 단어의 색인값 저장
            last_idx += 1
            table[letter + msg[idx]] = last_idx
            # 현재 입력 = '다음 단어'로 저장
            letter = msg[idx]
            # 다음 단어
            idx += 1
            continue
        # 이미 색인되어 있는 단어의 경우, 다음 단어를 현재 입력에 추가
        letter += msg[idx] # 여기 이해안되는데, 이미 사전에 있는 경우엔, 나중에 추가하는거여?난 바로 추가할 줄 알았는디
        # 그냥 로직상 어차피 if문 걸리면 append 해야되니까 여긴 안쓴건가.
        idx += 1
    answer.append(table[letter])
    return answer

print(solution(msg))
