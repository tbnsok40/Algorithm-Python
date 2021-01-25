# def solution(msg):
#     table = dict()
#     for idx, value in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ",1):
#         table[value] = idx
#         last_idx = idx
#     idx = 1
#     answer = []
#     letter = msg[0]
#     while idx < len(msg):
#         # 현재 입력 + 다음 글자 조합이 색인에 없는 경우
#         if letter + msg[idx] not in table:
#             # 현재 입력을 answer 배열에 저장
#             answer.append(table[letter])
#             # 새 단어의 색인값 저장
#             last_idx += 1
#             table[letter + msg[idx]] = last_idx
#             # 현재 입력 = '다음 단어'로 저장
#             letter = msg[idx]
#             # 다음 단어
#             idx += 1
#             continue
#         # 이미 색인되어 있는 단어의 경우, 다음 단어를 현재 입력에 추가
#         letter += msg[idx] # 여기 이해안되는데, 이미 사전에 있는 경우엔, 나중에 추가하는거여?난 바로 추가할 줄 알았는디
#         # 그냥 로직상 어차피 if문 걸리면 append 해야되니까 여긴 안쓴건가.
#         idx += 1
#     answer.append(table[letter])
#     return answer

def solution(msg):
    table = dict()
    for idx, value in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1):
        table[value] = idx
        last_idx = idx
# table에 없는 수가 나올 때까지 더한다.
    idx = 1
    curr = msg[0]
    ans = list()
    while idx < len(msg):
        if curr + msg[idx] not in table:
            last_idx += 1
            table[curr + msg[idx]] = last_idx
            ans.append(table[curr])

            curr = msg[idx]
            idx += 1
            continue
        curr += msg[idx]
        idx += 1
    ans.append(table[curr])
    return ans

msg = 'ABABABABABABABAB'
msg = 'KAKAO'

print(solution(msg))



