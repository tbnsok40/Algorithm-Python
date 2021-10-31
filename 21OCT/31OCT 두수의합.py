import sys

inputs = sys.stdin.readline().rstrip()
array = list(map(int, sys.stdin.readline().split()))
total = sys.stdin.readline().rstrip()

num_dict = dict()
count = 0

for i in array:
    num_dict[i] = 1
for n in array:
    if num_dict.get((int(total) - n)):
        count += 1

print(count // 2)

"""
9
5 12 7 10 9 1 2 3 11
13

서로 다른 수로 이루어져 있다.
해쉬를 만들수있단거지.
"""