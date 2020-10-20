def solution(skill, skill_trees):
    dict_s = dict()
    for letter in (skill):
        dict_s[letter] = 1

    count = 0
    for one in skill_trees:
        answer = ''
        for letter in one:
            if letter in dict_s:
                answer += letter
        if skill[:len(answer)] == answer:
            count += 1
    return count
skill = 'CBD'
skill_trees = ['BACDE', 'CBADF', 'AECB', 'BDA']
print(solution(skill,skill_trees))


# 오답
# def solution(skill, skill_trees):
#
#     dict_s = dict()
#     for idx,letter in enumerate(skill):
#         dict_s[letter] = idx
#
#     count = 0
#     for one in skill_trees:
#         answer = []
#         for letter in one:
#             try:
#                 answer.append(dict_s[letter])
#             except KeyError:
#                 pass
#
#         if answer[0] != 0:
#             continue
#         else:
#             if len(answer)-1 == answer[-1]:
#                 count += 1
#
#     return count