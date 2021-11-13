import sys

bracket = {
    ']': '[',
    ')': '('
}
while True:
    flag = True
    string = (sys.stdin.readline().rstrip())
    if string == '.':
        break

    stack = []
    for s in string:
        if s in ['[', '(']:
            stack.append(s)
        elif s in [']', ')']:
            if len(stack) > 0 and stack[-1] == bracket[s]:
                stack.pop()
            else:
                flag = False
                break

    if not flag:
        print('no')
    else:
        if not stack:
            print('yes')
        else:
            print('no')

"""
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
"""
