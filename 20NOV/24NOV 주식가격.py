prices = [1,2,3,2,3]
from collections import deque
def solution(prices):

    queue_prices = deque(prices)
    result = []
    while queue_prices:
        pops = queue_prices.popleft()
        count = 0
        for i in queue_prices:
            count += 1
            if pops > i:
                break
        result.append(count)
    return result

# 다른 사람 풀이
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer