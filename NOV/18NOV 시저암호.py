def solution(s, n):
    answer = ''
    return answer

n = 4
s = "a B z"
# print(solution(s,n))

s='a z'
d = 'A Z'
for i in s:
    print(ord(i))

for i in d:
    print(ord(i))

# 공백은 32
# a~z: 97 ~ 122
# A~Z: 65 ~ 90

# 90 + 1 = 91 = 65
# 90 + 2 = 92 = 66

# 91 - 26 = 65
n % 26 만큼 움직여야
if i + (n % 26) <= 90:
    i + (n % 26)
else:
    (i + (n % 26)) % 90 + 65