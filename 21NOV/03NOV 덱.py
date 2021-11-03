import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
numbers = deque()

for _ in range(N):
    commands = sys.stdin.readline().split()
    if commands[0] == "push_back":
        numbers.append(commands[1])
    if commands[0] == "push_front":
        numbers.appendleft(commands[1])
    if commands[0] == "front":
        if numbers:
            print(numbers[0])
        else:
            print(-1)
    if commands[0] == "back":
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
    if commands[0] == "pop_back":
        if numbers:
            print(numbers.pop())
        else:
            print(-1)
    if commands[0] == "pop_front":
        if numbers:
            print(numbers.popleft())
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
