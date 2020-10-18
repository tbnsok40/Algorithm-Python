# skill의 순서: 딕셔너리로 숫자 키 생성
# skill의 요소들을 iter 시키면서 리스트 인덱싱
# 첫번째 스킬은 무조건 나와야한다. 그렇지 않으면 뒤에 스킬들은 아예 불가
skill = "CBD"
skill_trees =["BACDE", "CBADF", "AECB", "BDA"]
# skill_trees = ['BACDE', 'CBADF', 'AECB', 'BDA', 'AQWER']
# def solution(skill, skill_trees):
#     answer = 0
#     for i in range(len(skill_trees)):
#         # print('-',i)
#         temp = list()
#         for idx, letter in enumerate(list(skill)):
#             if (idx == 0) and (letter not in skill_trees[i]):
#                 break
#             if letter in skill_trees[i]:
#                 temp.append(skill_trees[i].index(letter))
#
#         temp_original = temp
#         if len(temp) < 1:
#             answer += 1
#
#         if sorted(temp) == temp_original and len(temp)>0:
#             print(i,temp_original)
#             answer += 1
#     return answer

def solution(skill, skill_trees):
    cnt = 0
    for tree in skill_trees :
        a = [tree.index(i) for i in skill if i in tree]
        print(a)
        a_ = sorted(a)
        print([i in tree for i in skill[:len(a)]])
        if a == a_ and all(i in tree for i in skill[:len(a)]): cnt+=1
    return cnt

print(solution(skill,skill_trees))


