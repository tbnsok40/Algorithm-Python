import sys

inputs = [sys.stdin.readline().rstrip() for _ in range(3)]

result = 1
for i in inputs:
    result *= int(i)

for i in '0123456789':
    print(str(result).count(i))

# print(result)

"""
150
266
427
"""