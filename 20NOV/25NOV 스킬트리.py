def solution(skill, skill_trees):
    hash_dict = {}
    count = 0

    for idx, i in enumerate(skill):
        hash_dict[i] = idx

    for skills in skill_trees:
        temp = [-1]
        for j in skills:
            if (j in hash_dict) and (hash_dict[j] > max(temp)):
                temp.append(hash_dict[j])

        if len(temp) - 2 == max(temp):
            count += 1

    return count