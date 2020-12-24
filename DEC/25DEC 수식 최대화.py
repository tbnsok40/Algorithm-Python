from itertools import permutations

def solution(s):
    re_count = ['*', '+', '-']
    count = []
    for i in s:
        if i in re_count and i not in count:
            count.append(i)

    origin = []
    small = ''
    for i in s:
        if i not in count:
            small += i
        else:
            origin.append(small)
            small = ''
            origin.append(i)
    origin.append(small)

    ans = []
    for i in permutations(count, len(count)):
        temp = origin[:]
        result = count_permu(temp, i)
        ans.append(result)

    return max(ans)


def count_permu(temp, permus):
    # print(permus)
    for i in permus:
        for idx, j in enumerate(temp):
            if j == i:
                re = (eval(''.join(temp[idx - 1: idx + 2])))
                temp[idx] = str(re) # str() 처리를 안해주면 join에서 int로 인식되기에 오류
                del temp[idx + 1]
                del temp[idx - 1]

    if len(temp) > 1:
        return abs(eval(''.join(temp)))
    else:
        return abs(int(temp[0]))


# s = "100-200*300-500+20"
# s = "50*6-3*2"
# s = '100*4'

# s = '2-990-5+2' #995 연산자 우선순위 +>-
s = "2-990-5+2+3*2" #1996 연산자 우선순위 +>- >*
print(solution(s))

# 컴비네이션(X) 순열(permutation)으로 6가지 조합 만든후 연산 시행
# 답 보지 말 것

# 순열 대로 인덱스화 count[0],count[1],count[2]

# 큰 리스트를 만들고,
# 내부에 숫자별로, 연산자별로 구분한다.



# count = ['*', '+', '-']
# temp = []
# small = ''
# for i in s:
#     if i not in count:
#         small += i
#     else:
#         temp.append(small)
#         small = ''
#         temp.append(i)
# temp.append(small)
# print(eval(''.join(temp[2:5])))
# print(temp)

# 1. permutation 생성 함수
# 2. 그 퍼뮤테이션을 연산하는 함수
# 3. 연산 결과를 다시 1번 함수로 abs() 씌운채 리턴하여 result에 저장.
# 4. 여기서 max를 고른다.

# 2가 제일 문제
# (영상 찍을 때, 아 내 생각 방법따윈 안궁금하고!, 코드나 내놔! 하시는 분들은 몇분으로 넘어가세용)
