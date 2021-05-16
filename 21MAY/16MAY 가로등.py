def solution(road_length: int, locations: list):
    locations.sort()

    left = 1
    right = road_length

    while left <= right:
        # mid를 빛의 범위로 정의 => 점차 줄여나간다 이진 탐색 처럼
        mid = (left + right) // 2
        if is_possible(road_length, locations, mid):  # True 일 때
            right = mid - 1
        else:
            left = mid + 1
    return right + 1


def is_possible(road_length, locations, light_range):
    # locations[0], locations[-1]이 꼭 road의 시작점과 끝점에 있다는 생각이 함정으로 이어진다.
    # locations[0], locations[-1] 은 첫번째와 마지막 가로등일 뿐이지, 이들의 위치가 꼭 road의 시작점과 끝점에 있을 필요는 없다.
    if (0 < locations[0] - light_range) or (locations[-1] + light_range < road_length):
        return False
    for i in range(1, len(locations)):
        if locations[i - 1] + light_range < locations[i] - light_range:  # 가로등 간 공백이 생기는 경우
            return False
    return True


def solution(road_length, locations):
    locations.sort()
    print(locations)
    distance_list = []  # 가로등 사이의 거리

    if 0 < locations[0]:
        distance_list.append(locations[0])

    # 가로등 사이의 최소 거리
    for x, y in zip(locations[1:], locations[:-1]):
        if (x - y) % 2 == 0:
            distance = (x - y) // 2
        else:
            distance = (x - y) // 2 + 1
        print(x, y, distance)
        distance_list.append(distance)

    # v의 원소가
    if road_length > locations[-1]:
        distance_list.append(road_length - locations[-1])
    # print(distance_list)
    return max(distance_list)

# distance를 그냥 가장 크게 잡아 넣으면, 모든 거리를 다 비출 수 있다.
# 하지만 우리가 구하고자 하는 값은, 모든 거리를 다 비출 수 있는 distance 중 가장 작은 값을 구하는 것
# d_list엔 가로등 사이사이를 다 커버할 수 있는 distance의 범위가 들어있다. 이중에서 최소값을 구하면, 어떤 곳은 커버하고, 다른 곳은 커버할 수 없는 경우가 발생한다.
# 그렇기 때문에 d_list의 값 중 가장 큰 값을 선택하는 것이 옳다 (가장 큰 값: 가로등 사이가 가장 많이 떨어져 있는 경우의 distance)


road_length = 15
locations = [15,5,3,7,9,14,0]
print(solution(road_length, locations))