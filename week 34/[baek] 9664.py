import sys
def read(): return int(sys.stdin.readline())

daughters = read()
remains = read()

N = daughters-1
M = remains//N
if N*M < remains:
    fragments = remains - (N*M)
    ans = fragments + daughters*M
    print(ans, ans)
else:
    print(M*(daughters)-1, M*(daughters))