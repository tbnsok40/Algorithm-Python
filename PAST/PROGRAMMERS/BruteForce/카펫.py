def solution(brown, yellow):
    num = brown+yellow
    answer =[]
    for i in range(1,num):
        if (num / i) == (num//i):
            j = num //i
            print(num,i,j)
            if (i-2)*(j-2) == yellow:
                answer = [i,j]


    return answer
# print(solution(10,2))
# print(solution(8,1))
print(solution(24,24))