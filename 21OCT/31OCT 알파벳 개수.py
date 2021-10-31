import sys

inputs = sys.stdin.readline().rstrip()
w_dict = dict()
for w in inputs:
    w_dict[w] = w_dict.get(w, 0) + 1

answer = ''
for w in "abcdefghijklmnopqrstuvwxyz":
    answer += (str(w_dict.get(w, 0)) + ' ')
print(answer)


"""
baekjoon
"""
