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
name = "BBBAAAB" #9
# name = "ABABAAAAABA" #11

# 시작점 바로옆에 A가 붙어있으면, 그 반대쪽으로 순회 시작해야한다.
def solution(name):
    if len(name) == 1:
        return 0
    vertical = [91 - ord(string) if ord(string) > 78 else ord(string) - 65 for string in name]
    if 'A' not in name:
        horizon = len(name) - 1
        return horizon + sum(vertical)

    # 그냥 양쪽으로 다가봐
    # 슬라이싱

    name = list(name)
    for i in range(len(name)):
        rest = name[i + 1:]
        if len(rest) == rest.count('A'):
            store_r = i
            break
        elif len(rest) > len(name[:i]) + (len(rest)-rest.count('A')):
            store_r = len(name[:i]) + (len(rest)-rest.count('A'))
            break
    for i in range(len(name), 0, -1):
        rest = name[1:i]
        if len(rest) == rest.count('A'):
            store_l = len(name) - i
            break
        elif len(rest) > len(name[:i]) + (len(rest) - rest.count('A')):
            store_l = len(name[:i]) + (len(rest)-rest.count('A'))
            break

    if store_l <= store_r:
        return sum(vertical) + store_l
    else:
        return sum(vertical) + store_r


print(solution(name))