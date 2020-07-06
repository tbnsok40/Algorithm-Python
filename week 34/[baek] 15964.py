import sys
def read(): return map(int, sys.stdin.readline().split())
a, b = read()
print((a+b)*(a-b))