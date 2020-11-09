def solution(d, budget):

    if sum(d) == budget:
        return len(d)

d = [1,3,2,5,4]
budget = 9

d = [2,2,3,3]
budget = 10
print(solution(d,budget))

