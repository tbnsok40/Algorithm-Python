from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer, temp = 0, 0
    ongoing = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    while truck_weights or ongoing:
        temp -= ongoing.popleft()
        try:
            total = temp + truck_weights[0]
            if (total <= weight) and (len(ongoing) - 1 == bridge_length):
                head = truck_weights.popleft()
                ongoing.append(head)
                temp += head
            else:
                if total <= weight:
                    head = truck_weights.popleft()
                    ongoing.append(head)
                    temp += head
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

# 시간 실패 경우 => sum(ongoing)은 시간복잡도가 O(N), sum()메소드를 매번 사용하지 않고 ongoing의 출입 만으로 대체할 수 있다.
