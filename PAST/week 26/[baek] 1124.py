# a, b = map(int,input().split())
# 노소수 = list()
# 소수 = list()
# for j in range(a,b+1):
#     for i in range(2,j):
#         if (j % i) == 0:
#             노소수.append(j) #여기 들어간 j는 소수다.?
#             break
#     else:
#         소수.append(j)
#
# # 1. 소수가 아닌 것들 판별(소수가 아닌 애들이 후보)
# # 2. 얘들은 소인수분해했을때 x개의 소인수가 나오는데, 그 x가 소수여야한다.
# # 3. 그럼 이 x에 대해서 step1에서 했던 검사를 해주면 되는데, 처음 step1에서 메모리제이션을 해주면 어떨까?
# print(노소수)
# print(소수)
# count =0
# answer = []
# for i in range(len(노소수)):
#     a = 노소수[i]
#     for j in range(2,a):
#         if a // j ==0:
#             if a // j*j == 0:
#                 count += 2
#                 continue
#             count +=1
#     if count in 소수:
#         answer.append(a)
# count 다시 잘 짜봐래+에라토스테네스

# import sys
# r_input = sys.stdin.readline() # standard_input
# array = list()
# def run():
#     a, b = map(int, r_input().split())
#     for i in range(a,b+1):
#         array.append(i)
#     print(array)
#
#     return True
#
# if __name__ == '__main__':
#     run()


# 에라토스테네스의 체

# array = list()
# a,b = map(int, input().split())
# for i in range(a,b+1):
#     array.append(i)
est = [0]
for i in range(1, 10001):
    est.append(1)

for i in range(4,10001,2):
    est[i] = 0
for i in range(6,10001,3):
    est[i] = 0
for i in range(10,10001,5):
    est[i] = 0
for i in range(14,10001,7):
    est[i] = 0
for i in range(22,10001,11):
    est[i] = 0
    
print((est))