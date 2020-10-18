n = 5
p = [0, 20, 30, 35, 12, 3, 0]
w = [0, 2, 5, 7, 3, 1, 0]
pw = [0, 10, 6, 5, 4, 3, 0]
include = [0, 0, 0, 0, 0]
W = 9
maxprofit = 0

def promising(i, profit, weight):
    global j, k
    global totweight
    if (weight >= W):                               # 한도 무게 초과 시 return 0
        return 0
    else:                                           # 한도 무게 초과 X일 때
        j = i + 1                                   # 해당노드 다음 노드 할당
        bound = profit                              # bound 업데이트
        totweight = weight                          # totweight 업데이트
        while (j <= n and totweight + w[j] <= W):   # (j가 n보다 높지 않을 때) and (totweight + W[j] <= W 일 때)
            totweight = totweight + w[j]            # totweight 업데이트
            bound = bound + p[j]                    # bound 업데이트
            j = j + 1                               # j 업데이트
        k = j                                       # k 업데이트
        if (k <= n):
            bound = bound + (W - totweight) * (p[k] / w[k])     # bound 업데이트
        if (bound > maxprofit):                                 # maxprofit이 bound를 넘지 않는다면
            return 1                                            # return 1
        else:
            return 0

def knapsack(i, profit, weight):
    global numbest
    global maxprofit
    global include
    if (i <= n):                                                        # 노드가 n보다 작다면
        if (weight <= W and profit > maxprofit):                        # 현재 무게가 최대 무게보다 낮으면서, profit이 maxprofit보다 높을 때
            print(include, "weight:", weight, "maxprofit:", profit)
            maxprofit = profit                                          # maxprofit을 profit으로 update
            numbest = i                                                 # numbest를 현재 노드로 업데이트
                                                                        # bestset을 include로 업데이트
        if (promising(i, profit, weight) == 1):                         # 유망하면,
            include[i] = 1                                              # 해당 노드를 1로 업데이트 (트리에서 오른쪽)
            knapsack(i + 1, profit + p[i + 1], weight + w[i + 1])       # 그 다음 노드로 재귀호출
            include[i] = 0                                              # (트리에서 왼쪽으로)
            knapsack(i + 1, profit, weight)                             # 없는 상태로 재귀돌리기

knapsack(0, 0, 0)
