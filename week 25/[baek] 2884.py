# hour, min = input().split()
# hour, min = int(hour), int(min)
# while (0<=hour<=23) &(0<=min<=59):
#     if (min - 45) < 0:
#         res = min - 45
#         min = 60 + res
#         hour -= 1
#
#         if (hour) < 0:
#             hour = 23
#
#     else:
#         res = min - 45
#         min = res
#
#     print(hour, min)
#     break
#
a, b = map(int, input().split()); x= a*60 + b-45;print(x//60%24, x%60)