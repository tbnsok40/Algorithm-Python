import sys

inputs = sys.stdin.readline().rstrip()
num_dict = dict()
for i in str(inputs):
    num_dict[i] = (num_dict.get(i, 0) + 1)

print(max(num_dict.values()))


