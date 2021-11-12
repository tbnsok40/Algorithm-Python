import sys


string = sys.stdin.readline().rstrip()
str_dict = {}
for idx, s in enumerate(list(string)):
    if s not in str_dict:
        str_dict[s] = idx
result = list()
for s in "abcdefghijklmnopqrstuvwxyz":
    r = str_dict.get(s, -1)
    result.append(r)
print(*result)
