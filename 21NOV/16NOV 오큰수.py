import sys

N = int(input())  # N = 100000 일 때
arr = list(map(int, sys.stdin.readline().split()))
result = [-1] * N
stack = [0]
# for i in range(N):
#     if i == N - 1:
#         result[i] = -1
#     else:
#         if max(arr[i + 1:]) > arr[i]:  # 시간 초과 피하려고 조건 걸어봤지만 nope
#             for j in arr[i + 1:]:
#                 if arr[i] < j and result[i] == -1:
#                     result[i] = j
#         else:
#             continue

"""
이중 for 시간초과 문제는 stack 을 이용하여 풀 수 있다.
"""
for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        pops = stack.pop()
        print('i =', i,' pops =', pops)

        result[pops] = arr[i]
    stack.append(i)


print(result)
# 시간 초과
