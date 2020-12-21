s = 'baabaa'
# s = 'cdbbdc'
# s = 'acddcdda'
# def solution(s):
#     N = len(s)
#     front = s[:N//2]
#     rear = s[N//2:]
#     if N % 2 != 0:
#         return 0
#     if (front == rear) and (N // 2) % 2 != 0:
#         return 1
#     elif front == rear[::-1]:
#         return 1
#     else:
#         return 0

def solution(s):
    s = list(s)
    count = 0
    N = len(s)
    while s:
        for idx, i in enumerate(s):
            try:
                if s[idx] == s[idx + 1]:
                    s.remove(s[idx]), s.remove(s[idx])
                    break
            except:
                pass
        count += 1
        if count > (N) + 1:
            return 0
    return 1

print(solution(s))
