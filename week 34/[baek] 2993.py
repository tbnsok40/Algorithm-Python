# strings = list(input())
# print(strings) # list는 모두 한letter단위로 반환한다.
import sys
def read(): return sys.stdin.readline()

before = read()
# for i in range(len(before)):
#     for j in range(i+2,len(before)):
#         first = before[:i+1]
#         mid = before[i+1:j]
#         last = before[j:]
#         first.reverse()

print(('').join(reversed(before)))
print(before[::-1])