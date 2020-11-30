def solution(s):
    if len(s) is 1:
        return 1
    min_sum = len(s)
    for i in range(1, (len(s) // 2) + 1):
        result = []
        for j in range(0, len(s)):
            result.append(s[j * i: j * i + i])
        result.append('') # 마지막 못 들어간 문자 처리하기 위한 장치
        sum = ""
        temp = ""
        count = 1
        for k in range(len(result) - 1):
            if result[k] == result[k + 1]:
                count += 1
            else:
                if count == 1:
                    temp = result[k]
                else:
                    temp = str(count) + result[k]
                    count = 1
                sum += temp
        if len(sum) < min_sum:
            min_sum = len(sum)
    return min_sum


# 사실 몇이 더해지느냐는 전혀 중요한 문제가 아니다, 1이 더해지든 2가 더해지든 길이는 같다.
# 100이 더해지면 문제긴 한데