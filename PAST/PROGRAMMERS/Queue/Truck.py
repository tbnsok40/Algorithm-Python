truck_list1 = [10,10,10,10,10,10,10,10,10,10]
truck_list2 = [10]
truck_list3 = [7,4,5,6]

def solution(bridge_length, weight, truck_list):
    time = 0
    temp = 0
    bridge = [0 for _ in range(bridge_length)]
    while bridge:
        time += 1
        out = bridge.pop(0)
        temp -= out
        # print(time, temp)
        if truck_list:
            if truck_list[0] + temp <= weight:
                curr = truck_list.pop(0)
                bridge.append(curr)
                temp += curr
            else:
                bridge.append(0)
    return time
print(solution(100,100,truck_list1))
print(solution(100,100,truck_list2))
print(solution(2,10,truck_list3))
