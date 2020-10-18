# N, P = map(int, input().split())
# W, L, maxScore = map(int, input().split())  # max를 변수로 지정해버리면 메서드를 못슨다.
# name_set = set()
# game_set = list()
# sum = 0
# for n in range(P):
#     name, wl = (input().split())
#     if wl == 'W':
#         name_set.add(name)
# for n in range(N):
#     player = input()
#     game_set.append((player))
#
# for i in range(N):
#     if i != N-1:
#         if game_set[i] in name_set:
#             sum += W
#             if sum >= maxScore:
#                 print('I AM NOT IRONMAN!!')
#                 break
#         else:
#             sum -= L
#             if sum < 0:
#                 sum = 0
#     else:
#         if game_set[i] in name_set:
#             sum += W
#             if sum >= maxScore:
#                 print('I AM NOT IRONMAN!!')
#             else:
#                 print("I AM IRONMAN!!")
#         else:
#             print('I AM IRONMAN!!')
#
# # sum이 maxScore를 넘겨버릴 수 있다.

# input = __import__('sys').stdin.readline
# n, m = map(int, input().split())
# w, l, g = map(int, input().split())
# s = { u for u, v in (input().split() for _ in range(m)) if v == 'W' }
# t = 0
# for _ in range(n):
# 	if input()[:-1] in s: t += w
#
# 	else: t = max(0, t - l)
# 	if t >= g:
# 		print('I AM NOT IRONMAN!!')
# 		exit()
# print('I AM IRONMAN!!')