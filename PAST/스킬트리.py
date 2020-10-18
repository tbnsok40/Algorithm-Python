skill = ['CBD']
skill_trees = ['BACDE', 'CBADF', 'AECB', 'BDA']
# skill 순서 앞지르는 경우 유의
def solution(skill, skill_trees):
    answer =0
    letters = list(skill[0])

    for skills in skill_trees:
        temp = []
        for letter in letters:

            if letter in skills:
                temp.append(skills.index(letter))
        if temp == sorted(temp):
            answer += 1
            print(skills, answer)
solution(skill,skill_trees)