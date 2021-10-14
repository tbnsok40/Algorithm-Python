def solution(registered_list, new_id):
    registered_dict = dict()
    for registered in registered_list:
        registered_dict[registered] = 1

    # new_id 가 registered_list 에 없는 경우
    if new_id not in registered_list:
        return new_id

    # new_id 가 registered_list 이미 존재하는 경우
    length = len(new_id)
    num_start_idx = 0
    for idx in range(length):
        if new_id[idx].isalpha():
            num_start_idx = idx
        else:
            break

    strings = new_id[:num_start_idx + 1]
    if new_id[num_start_idx + 1:]:
        next_nums = int(new_id[num_start_idx + 1:]) + 1
    else:
        next_nums = 1

    while True:
        new_id = strings + str(next_nums)
        if new_id in registered_dict:
            next_nums = int(new_id[num_start_idx + 1:]) + 1
            continue
        else:
            return new_id



registered_list = ["apple1", "orange", "banana3"]
new_id = "apple"

print(solution(registered_list, new_id))
