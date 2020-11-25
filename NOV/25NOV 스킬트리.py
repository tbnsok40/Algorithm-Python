def solution(skill, skill_trees):
    hash_dict = {}
    for idx, i in enumerate(skill):
        hash_dict[i] = idx
    count = 0
    for skills in skill_trees: # O(n)
        temp = [-1]

        for j in skills:
            if (j in hash_dict) and (hash_dict[j] > max(temp)):
                temp.append(hash_dict[j])
        # print(skills, temp)
        if len(temp) - 2 == max(temp):
            # print(skills,temp)
            count += 1

    return count
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))