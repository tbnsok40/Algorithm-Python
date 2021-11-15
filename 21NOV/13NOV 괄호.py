import sys


N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    stack = []
    bracket = sys.stdin.readline().rstrip()
    flag = True
    for b in bracket:
        if b == '(':
            stack.append(b)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                flag = False
                break
    if flag:
        if len(stack) > 0:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")




"""
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
"""
