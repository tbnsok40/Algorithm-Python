import sys
def read(): return int(sys.stdin.readline())

daughters = read()
remains = read()

N = daughters-1
M = remains//N
print(M*(daughters)-1, M*(daughters))