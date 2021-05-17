# 1개 일치: 6등
# 2개: 5
# 3개: 4
# 4개: 3
# 5개: 2
# 6개: 1등

# 오답
def solution(lottos, win_nums):
    count_zero = lottos.count(0)
    count = [1 for num in lottos if num in win_nums]

    if not count:
        return [1, 6]
    # 하나도 맞은게 없다는 것(count 가 0)은 2가지로 분류 되는데,
    # 1) 모두 0이라 맞은게 없을 땐 [1,6]이 되고,
    # 2) 0이 하나도 없을 땐, [6,6]이 된다.
    # 이 점을 간과하여 14번 케이스를 뚫지 못했다. (1번 케이스만 생각한거지)

    return [7 - (len(count) + count_zero), 7 - len(count)]


# 정답
def solution(lottos, win_nums):
    count_zero = lottos.count(0)
    count = [1 for num in lottos if num in win_nums]
    if (count_zero) == 6:
        return [1, 6]
    elif not count:
        return [6, 6]
    else:
        return [7 - (len(count) + count_zero), 7 - len(count)]