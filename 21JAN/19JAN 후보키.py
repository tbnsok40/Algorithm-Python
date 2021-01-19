from itertools import combinations
def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])
    candidates, final = [], []

    for i in range(1, n_col + 1):
        # extends는 appends의 확장(원소 레벨을 넘어 iter까지 넣어버린다)
        candidates.extend(combinations(range(n_col), i))
    # 유일성
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation] # 자칫 다중 for문 될 것 같은데..?
        if len(set(tmp)) == n_row: # 중복된게 없다
            final.append(keys) # 유일성 만족한 상태 but 최소성은 아직 불만족

    #최소성
    answer = set(final)
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])
    # print(answer)
    return len(answer)
relation = [["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"]]
print(solution(relation))

# set은 중복 허용안하니까 리스트와 세트와 길이 비교했을 때 같은거 리턴
