# 자리마다 이동해야할 숫자 존재

# 1. 에이부터 시작하므로, 위로가 빠를지 아래로가 빠를지 계산
# 2. 맥스가 13.미니멈은 0
# 3. 0이 있는 부분은 굳이 안가도 된다 그게 효율적.

# N, O 사이


# 수평으로 0이 놓여져있는걸 어떻게 효율적으로 계산하는냐가 관건
# 첫 자리를 기준으로 양옆에 0과의 거리가
# 78보다 큰 숫자는 91에서 빼주는게 낫다

# name에 A가 없는 경우는 바로 삭 가능


name = "JEROEN"
# name = "BBBAAAB" #9
# name = "ABABAAAAABA" #11

# 시작점 바로옆에 A가 붙어있으면, 그 반대쪽으로 순회 시작해야한다.

def solution(name):
    vertical = [min(91 - ord(string), ord(string) - 65) for string in name]
    answer = sum(vertical)
    name = list(name)
    index = 0
    N = len(name)

    while True:
        right = 1
        left = 1
        name[index] = 'A'

        if name == ['A'] * N: break

        for i in range(1, N):
            if name[index + i] == 'A': right += 1
            else: break

        for i in range(1, N):
            if name[index-i]=="A": left+=1
            else: break

        if right>left:
            answer+=left
            index-=left
        else:
            answer+=right
            index+=right

    return answer



# 다른 사람 풀이
def solution(name):
    answer = 0
    name=list(name)
    index=0
    while(True):
        right=1
        left=1
        if name[index] != 'A':
            updown = min(ord(name[index])-ord('A'),(ord('Z')-ord(name[index])+1))
            answer += updown
        name[index] = 'A'
        if name == ["A"]*len(name): break
        for i in range(1,len(name)):
            if name[index+i]=="A": right+=1
            else: break
        for i in range(1,len(name)):
            if name[index-i]=="A": left+=1
            else: break
        if right>left:
            answer+=left
            index-=left
        else:
            answer+=right
            index+=right
    return answer


# 알게된 사실: 파이썬 문자열은 슬라이싱은 제공하지만, item assignment는 제공하지 않는다