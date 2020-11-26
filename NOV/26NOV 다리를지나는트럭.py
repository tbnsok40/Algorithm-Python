from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    ongoing = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    while truck_weights or ongoing:
        print(truck_weights, ongoing)

        ongoing.popleft()
        try:
            if (sum(ongoing) + truck_weights[0] <= weight) and (len(ongoing) - 1 == bridge_length):
                head = truck_weights.popleft()
                ongoing.append(head)
            else:
                if sum(ongoing) + truck_weights[0] <= weight:
                    ongoing.append(truck_weights.popleft())
                else:
                    ongoing.append(0)
        except:
            pass
        answer += 1
    return answer
#1. 무게 만족 / 길이 불만족
# => og.popleft(), og.append(head)
#2. 무게 불만족/ 길이 만족
# => og.popleft(), og.append(0)
#3. 둘다 불만족
# => og.popleft(),
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))