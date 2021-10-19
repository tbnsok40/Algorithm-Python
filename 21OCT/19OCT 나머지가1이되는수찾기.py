def solution(n):

    temp = n - 1

    if temp % 2 != 0:
        if temp % 3 != 0:
            return temp
        else:
            return 3
    else:
        return 2

# 192 => 191

# 21 , 2 => 21 - 1 = 20 => 20의 1이 아닌 최소약수: 2
# 30, 29
# 반례 26 => 5로 나누어 떨어지는 경우도 생각해야.
print(solution(26))