def solution(n):
    cnt = 0

    while n > 0:
        q, r = divmod(n, 2)
        if r != 0:
            cnt += 1
        n = q
    return cnt

# 1. n을 분해해야하나? ㅇㅇ
# 2. n이 0이 되기 전까지 분해
# 3. n % 2
