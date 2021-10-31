import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()

for i in range(N):
    cmds = sys.stdin.readline().split()
    cmd = cmds[0]

    if cmd == "push":
        # queue.insert(0, cmds[1])
        queue.append(cmds[1])
    elif cmd == "pop":
        if len(queue):
            pops = queue.popleft()
            print(pops)
        else:
            print(-1)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        if len(queue):
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif cmd == "back":
        if len(queue):
            print(queue[-1])
        else:
            print(-1)

"""
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
"""
