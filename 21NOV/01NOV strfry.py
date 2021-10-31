import sys

N = sys.stdin.readline().rstrip()

for _ in range(int(N)):
    before, after = sys.stdin.readline().split()
    before = ''.join(sorted(list(before)))
    after = ''.join(sorted(list(after)))
    if len(before) != len(after):
        print("Impossible")
        continue
    for i in range(len(before)):
        if before[i] != after[i]:
            print("Impossible")
            break
    else:
        print("Possible")
""""
4
a a
ab ba
ring gnir
newt twan

간과한 점: 문자 원소는 모두 일치해도 서로 길이가 달라질 수 있다. 그럼 strfry 임파서블인 것.
"""