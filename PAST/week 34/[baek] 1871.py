import string
import sys

def alpha_to_num(s):
    return (string.ascii_uppercase.index(s))

N = int(sys.stdin.readline())
for _ in range(N):
    strings = (input().split('-'))
    sum = 0
    for i in range(3):
        # print(alpha_to_num(strings[0][i]) * 26 **(2 - i))
        sum += alpha_to_num(strings[0][i])*26**(2-i)

        # print(alpha_to_num(strings[0][i]))
    # print(sum)
    if abs(sum - int(strings[1])) <= 100:
        print('nice')
    else:
        print('not nice')
