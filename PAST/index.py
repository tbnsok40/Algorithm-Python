#1


# 2
def problem2():
    print('2번 문제')
    num = input('입력: ')
    # 숫자 갯수 카운팅
    count = 0
    for i in num:
        if i == '[':
            count += 1

    # 숫자만큼 돌리기
    answer = ''
    for _ in range(count):
        alpha = ''
        for idx, i in enumerate(num):
            if i != '[':
                alpha += i
            elif i == '[':
                alpha = int(alpha)
                num = num[idx+1:]
                break
        letter = ''
        for idx, j in enumerate(num):
            if j != ']':
                letter += j
            elif j == ']':
                answer += letter * alpha
                num = num[idx+1:]
                break
    return answer
print(problem2())

#3
import statistics

def problem3():
    print('3번 문제')
    num3 = int(input('입력: '))
    entire_score = list(map(int, input('입력: ').split()))
    each_person = list(map(int, input('입력: ').split()))

    answer = []
    total = 0

    entire_dict = dict()
    for a, b in zip(entire_score, each_person):
        total += a*b
        entire_dict[a] = b
    entire_keys = list(entire_dict.keys())
    avg = total / num3
    median = statistics.median(entire_score)
    print('전체 평균은 %d' %avg, '이고, 중간값은 %d' %median, '입니다.')
    for key in entire_dict:
        value = entire_dict[key]
        print('%d점을 받은 사람은' %key, '%d명이고' %value)
    print('시험을 본 전체수는 %d명입니다.' %sum(each_person))

    return ''
print(problem3())

#4 두가지 경우로 풀었습니다.(1.파이썬 메서드 활용, 2. 반복문 활용)
import random
number = []
def problem4(number, low, high, target):
    print('4번 문제')
    # 숫자 255개 랜덤 생성(중복없이)
    while len(number) < 255:
        num = random.randint(1, 1000)
        if num not in number:  # 새로운 수가 중복이 아니면,
            number.append(num)  # 리스트에 추가
    number.sort()  # 소팅

    # 첫번째 방법: 파이썬 메서드 사용
    if target in number:
        return (number.index(target))
    else:
        return -1

    # 두번째 방법: 반복문 사용
    # low -= low #인덱스 세팅
    # high -= high #인덱스 세팅
    # chance = 0
    # while chance < 8:
    #     mid = (low + high)//2
    #     if target == number[mid]:
    #         return mid
    #     elif target < number[mid]:
    #         number = number[:mid]
    #     else:
    #         number = number[mid:]
    #     chance += 1
    # return 'fail'
print(problem4(number, 1, 255, 100))


#5
def problem5():
    print('5번 문제')
    string = input('입력:')
    temp = string.split(' ')
    count_java, count_c = 0, 0

    for word in temp:
        if word == 'java':
            count_java += 1
        if word == 'c++':
            count_c += 1
    return 'java: %d 개' %count_java, 'c++: %d 개' %count_c
print(problem5())


def solution(n):
    temp = n
    for i in range(1,n):
        # print(temp)
        if temp - 3**i < 0:
            save_i = i
            break
        else:
            temp = temp - 3**i
print(solution(19))

def solution(n):
    temp = []
    if n < 2:
        return '01'[n]
    else:
        a, b = divmod(n, 2)
        init =  solution(a) + '01'[b]
    a = init.count('1')
    return a


# 124 진법
# def solution(n):
#     c = bin(n).count('1')
#     for m in range(n+1, 1000000):
#         if c == bin(m).count('1'):
#             return m
#
# print(solution(78))

# 2진법 문제

