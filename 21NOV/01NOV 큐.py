import sys
N = int(sys.stdin.readline())

queue = []

for i in range(N):
    cmds = sys.stdin.readline().split()
    cmd = cmds[0]
    # print(cmds, cmd)

    if cmd == "push":
        queue.insert(0, cmds[1])
    elif cmd == "pop":
        if len(queue):
            pops = queue.pop()
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
            print(queue[len(queue) - 1])
        else:
            print(-1)
    elif cmd == "back":
        if len(queue):
            print(queue[0])
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