import sys

N = list(sys.stdin.readline().rstrip())
result = [0] * 10
room_dict = dict()
total = 0
for i in range(len(N)):
    num = int(N[i])
    if num == 6 or num == 9:
        if result[6] <= result[9]:
            result[6] += 1
        else:
            result[9] += 1
    else:
        result[num] += 1
print(max(result))
"""
9999
122

"""
