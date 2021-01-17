# 조건: 완주하지 못한 선수는 무조건 한명 존재한다.
# 딕셔너리에 넣어도 되긴한데, 동명이인이 문제
# participant의 value와 competition의 value 차이가 1이상일 때 키 값 바로 리턴

participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

# 1
def solution(participant, completion):
    # temp = participant + completion
    # temp.sort() # 아래처럼 처리하는게 더 빠르다. sort()와 sorted()의 차이때문인가?
    
    temp = sorted(participant + completion)
    for i in range(0,len(temp),2):
        try:
            if temp[i] != temp[i+1]:
                return temp[i]
        except IndexError:
            return temp[-1]


# 2
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for par, com in zip(participant, completion):
        if par != com:
            return par  # 예시 1번

    return participant[-1]  # 예시 2번

# sorting해서 zip 묶어버리자 <= 이 방법은 없을까.