def solution(scores):
    scores_ = list(map(list, zip(*scores)))
    for s in scores_:
        print(s)
    N = len(scores)
    result = ''
    for i in range(N):
        end = scores_[i][i]
        if (end == min(scores_[i]) or end == max(scores_[i])) and (scores_[i].count(end) == 1):
            scores_[i][i] = 0
            mean = sum(scores_[i]) / (N - 1)
        else:
            mean = sum(scores_[i]) / N
        if mean >= 90:
            result += "A"
        elif 90 > mean >= 80:
            result += "B"
        elif 80 > mean >= 70:
            result += "C"
        elif 70 > mean >= 50:
            result += "D"
        else:
            result += 'F'
    return result


scores = [[100, 90, 98, 88, 65],
          [50, 45, 99, 85, 77],
          [47, 88, 95, 80, 67],
          [61, 57, 100, 80, 65],
          [24, 90, 94, 75, 65]]
print(solution(scores))
