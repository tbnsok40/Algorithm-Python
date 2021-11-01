import sys
from collections import Counter


a = Counter(list(sys.stdin.readline().rstrip()))
b = Counter(list(sys.stdin.readline().rstrip()))

print(sum((a - b).values()) + sum((b - a).values()))
"""
abcd
bccde
"""