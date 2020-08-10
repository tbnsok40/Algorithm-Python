prices = [1,2,3,2,3]
from collections import deque
def solution(prices):
    ans = []
    que_prices = deque(prices)
    while (que_prices):
        prices = que_prices.popleft()
        up_time = 0
        for n in que_prices:
            up_time += 1
            if prices > n:
                break
        ans.append(up_time)
    return ans

print(solution(prices))

# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         count_time = 0
#         for j in range(i+1,len(prices)):
#             count_time +=1
#             if prices[i] > prices[j]:
#                 break
#         answer.append(count_time)
#
#     return answer
#
# print(solution(prices))
