import sys

N = int(sys.stdin.readline().rstrip())
numbers = []
for _ in range(N):
    commands = sys.stdin.readline().split()
    if commands[0] == "push":
        numbers.append(commands[1])
    if commands[0] == "top":
        if numbers:
            print(numbers[-1])
        else:
            print(-1)
    if commands[0] == "size":
        print(len(numbers))
    if commands[0] == "empty":
        if numbers:
            print(0)
        else:
            print(1)
    if commands[0] == "pop":
        if numbers:
            print(numbers.pop())
        else:
            print(-1)

"""
14
push 1
push 2
top
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
top
"""
