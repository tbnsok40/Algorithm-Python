# import sys
# input = sys.stdin.readline
# T = int(input())
# numbers = [int(input()) for _ in range(T)]
# numbers = sorted(numbers, reverse=True)
# result = 0
# while len(numbers)>=3:
#     new = [] # 굳이 새 리스트를 만들 필요가 있었을까ㅏ.
#     for i in range(3):
#         new.append(numbers[i])
#     numbers = numbers[3:]
#     part_sum = sum(new) - min(new)
#     result += part_sum
# result += sum(numbers)
# print(result)

###############################
import sys
input = sys.stdin.readline
T = int(input())
numbers = [int(input()) for _ in range(T)]
numbers = sorted(numbers)
result = 0
while len(numbers)>=1:
    if len(numbers)>=3:
        result += numbers[len(numbers)-1] + numbers[len(numbers)-2]
        for _ in range(3):
            del numbers[-1]
        # print(numbers, result)
    else:
        result += sum(numbers)
        break
print(result)
