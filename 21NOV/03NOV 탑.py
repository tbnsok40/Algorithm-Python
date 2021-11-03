import sys

N = sys.stdin.readline().rstrip()
M = list(map(int, sys.stdin.readline().split()))
result = [0] * int(N)
for i in range(len(M) - 1, 0, -1):

    # before = i - 1
    current_idx = i
    current = M[i]
    max_value = max(M[0: i])
    if max_value < current:
        continue
        # result[i] = M.index(max_value)
    else:
        while True:
            i -= 1
            if M[i] >= current:
                result[current_idx] = i + 1
                break

print(*result)

"""
5
6 9 5 7 4

# 역으로 정렬?

"""
