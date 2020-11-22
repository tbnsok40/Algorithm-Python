# N: 스테이지 수/단계
# stages, 각 참가자가 머물고있는 '단계'
# 각 원소가 몇개인지, ex)1이 몇개인지, 4가 몇개인지 dictionary

def solution(N, stages):

    stage_dic = {}
    members = len(stages)
    for i in stages:
        try:
            stage_dic[i] += 1
        except:
            stage_dic[i] = 1

    result = {}
    for i in range(1, N + 1):
        try:
            result[i] = stage_dic[i] / members
            members = members - stage_dic[i]
        except:
            result[i] = 0

    result = sorted(result.items(), key = lambda x: x[1], reverse=True)
    return list(map(lambda x:x[0], result))


# 스스로 생각하는 법을 잊은
# 니들의 대표적인 병명은 선택장애