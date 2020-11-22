# N: 스테이지 수/단계
# stages, 각 참가자가 머물고있는 '단계'
# 각 원소가 몇개인지, ex)1이 몇개인지, 4가 몇개인지 dictionary
stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5

stages = [4, 4, 4, 4, 4]
N = 4
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

    # 31번 줄 처럼 한줄로 치환 가능 => 딕셔너리의 value를 기준으로 내림차순 정렬
    # result = sorted(result.items(), key = lambda x: x[1], reverse=True)
    # return list(map(lambda x:x[0], result))

    return sorted(result, key = lambda x: result[x], reverse=True)


# 스스로 생각하는 법을 잊은
# 니들의 대표적인 병명은 선택장애