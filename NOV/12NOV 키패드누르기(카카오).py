def solution(numbers, hand):
    left = (1,4,7)
    mid = (2,5,8)
    right = (3,6,9)
    answer = []
    for i in numbers:
        if i in left:
            answer.append('L')
            curr_l = i
        elif i in right:
            answer.append('R')
            curr_r = i
        else:
            


    return answer
print(solution([1,2],'right'))


