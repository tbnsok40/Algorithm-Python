from collections import Counter
v = [[1, 4], [3, 4], [3, 10]]
def solution(v):
    # 총 좌표의 x와 y의 갯수는 같아야한다.
    result = []
    for i in zip(*v):
        y = Counter(i)
        result.extend([i for i in y if y[i] == 1])
    return result

solution(v)