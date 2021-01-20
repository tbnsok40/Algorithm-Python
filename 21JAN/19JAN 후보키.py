from itertools import combinations
# 결국 삼중 for문이지만,
def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])
    candidates, final = [], []

    for i in range(1, n_col + 1):
        # extends는 appends의 확장(원소 레벨을 넘어 iter까지 넣어버린다)
        candidates.extend(combinations(range(n_col), i)) # range(n_col) 은 (0~4)를 나타내는 집합 같은 것, 일종의 iter

    # 유일성
    for keys in candidates:
        # 왜 굳이 tuple로 묶었지?
        tmp = set([tuple([item[key] for key in keys]) for item in relation])
        # for item in relation:
        #     print(set(tuple(item[key] for key in keys)))
        if len(tmp) == n_row: # 중복된게 없다/ set(tmp)를 하면, 중복원소가 있을 경우 하나로 퉁쳐진다. 그러게 있다면, n_row와 길이가 같을 수 없다.
            final.append(keys) # 유일성 만족한 상태 but 최소성은 아직 불만족
            # 결국 final에 남는 것은, 숫자값: 컬럼number(keys)
    # print(final)
    # # 최소성
    answer = set(final)
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            print(final[i], set(final[i]).intersection(set(final[j])), set(final[j]))
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])
    return len(answer)
# 기억이 잘 안나면 잘 된 것, 새로 풀어보자
relation = [["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"]]

print(solution(relation))

# set은 중복 허용안하니까 리스트와 세트와 길이 비교했을 때 같은거 리턴
