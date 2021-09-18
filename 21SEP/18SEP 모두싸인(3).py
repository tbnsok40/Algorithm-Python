def solution(n, k):
    i = 2
    while True:
        try:
            m = str(n) * i
            if int(m) % k == 0:
                return i
            i += 1
        finally:
            return -1


print(solution(n=2234567892, k=15))
