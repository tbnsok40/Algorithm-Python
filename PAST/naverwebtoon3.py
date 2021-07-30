def solution(play_list, listen_time):

    if sum(play_list) <= listen_time:
        return len(play_list)

    result = 0

    for idx, i in enumerate(play_list):
        for jdx, j in enumerate(play_list[idx:]):
            if listen_time > sum(play_list[idx: idx + jdx]):
                result = jdx + 1

    answer = 0
    return answer


play_list = [1, 2, 3, 4]
listen_time = 5

# play_list = [1, 2, 3, 4]
# listen_time = 20

print(solution(play_list, listen_time))
