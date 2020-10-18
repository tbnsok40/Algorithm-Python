import sys
T = int(sys.stdin.readline())
mts = list(map(int, sys.stdin.readline().split()))
maxi = -1
for i in range(len(mts)-1):
    if(maxi >= len(mts[i+1:])): break
    count = 0
    for j in range(i+1, len(mts)):
        if mts[i] > mts[j]:
            count += 1
        else: # 여기가 왜 있어야하지? => 문제 조건을 똑바로 읽자.
            break
    maxi = count if count > maxi else maxi
print(maxi)

# 피벗 오른쪽의 값들을 sort.
# sort된 리스트의 맥스값이, 피벗보다 작으면 바로 답 나와.(이러면 애초에 sort도 필요없지)
# 그게 아니면,,?
# 리스트 미니멈 값이 피벗보다 크면, 그것도 계산 할 필요 없지
# import sys
# T = int(sys.stdin.readline())
# mts = list(map(int, sys.stdin.readline().split()))

# T = input()
# # l = list(map(int, input().split())); L,M = len(l),0
# # for i in range(L):
# #     if(i>=1 and M>=len(l[i+1:])): break
# #     m = 0
# #     for j in range(i+1,L):
# #         if (l[i] > l[j]): m+=1
# #         else: break
# #     M = m if m > M else M
# # print(M)
