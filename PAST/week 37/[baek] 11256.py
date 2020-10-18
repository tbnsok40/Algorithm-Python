import sys
input = sys.stdin.readline

for _ in range(int(input())):
    candy, box = map(int, input().split())
    result = list()
    for _ in range(box):
        row, col = map(int, input().split())
        result.append(row*col)
    result = sorted(result, reverse=True)
    for idx,square in enumerate(result):
        candy -= square
        if candy <= 0:
            print(idx + 1)
            break



# answer = [list(map(int, input().split())) for _ in range(box)]