import sys

N = sys.stdin.readline().rstrip()
for _ in range(int(N)):
    a, b = sys.stdin.readline().split(" ")
    print(int(a) + int(b))