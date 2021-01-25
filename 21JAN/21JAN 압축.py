msg = 'ABABABABABABABAB'
# msg = 'KAKAO'
def solution(msg):
    table = dict()
    for idx, alphabet in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1):
        table[alphabet] = idx
    last_idx = idx
    ans = []
    curr = msg[0] # 단어 하나
    idx = 1
    while idx < len(msg):
        if curr + msg[idx] in table:
            curr += msg[idx]
            idx += 1
        else:
            ans.append(table[curr])
            last_idx += 1
            table[curr + msg[idx]] = last_idx
            curr = msg[idx]
            idx += 1
    ans.append(table[curr])
    return ans
print(solution(msg))

# point is that we r not gonna append to list(:ans) directly in the if statement

