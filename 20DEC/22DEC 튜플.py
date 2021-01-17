s= "{{1,2,3},{2,1},{1,2,4,3},{2}}"
# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
def solution(s):
    # s = '[' + s[1:-1] + ']'
    # s = eval(s)
    s = s[2:-2].split('},{')
    # s = list(map(set, s))
    print(len(s))
    temp = []
    for i in range(len(s)):
        S = s[i].split(',')
        temp.append(set(S))
    print((temp))
    # s.sort(key = lambda x: len(x))
    # result = []
    # result.append(*s[0])
    # for i in range(1, len(s)):
    #     result.append(*(s[i] - s[i-1]))
    # return result


def solution(s):
    s = '[' + s[1:-1] + ']'
    s = eval(s)
    s.sort(key=lambda x: len(x))
    result = [set()] + s
    final = []
    for i in range(1, len(result)):
        final.append(*(result[i] - result[i - 1]))
    return final

print(solution(s))
