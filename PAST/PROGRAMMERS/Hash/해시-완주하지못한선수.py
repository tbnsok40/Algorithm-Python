participant = ['mislav', 'stanko',  'ana','mislav']
completion = ['stanko', 'ana', 'mislav']

# hash() 내장함수의 특징을 살린 풀이
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += (hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer

def solution(participant, completion):
    answer = ''
    parti = dict()
    comple = dict()
    for name in participant:
        try:
            parti[name] += 1
        except KeyError:
            parti[name] = 1

    for name in completion:
        try:
            comple[name] += 1
        except KeyError:
            comple[name] = 1

    for name in parti:
        if parti[name] > 1:
            if parti[name] == comple[name]:
                pass
            else:
                answer = name
                break
        elif name not in comple:
            answer = name
            break
    return answer
print(solution(participant, completion))
