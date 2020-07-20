#####################코테####################
# 1번 문제, '봄'이 '봄봄'과 중복되는지 검사하는 것.
# 2번 문제, set() 메소드를 사용하지 않고, 합집합, 차집합, 교집합 등을 구하는 것
#1
name_list = ["너굴", "너울", "겨울", '개굴']

def check(name_list):
    new_list = []
    for name in name_list:
        if name not in new_list:
            new_list.append((name))
            answer = False
        else:
            answer = True
            break
    if answer == True:
        return answer
    else:
        return check_duplicate(name_list)

def check_duplicate(list):
    for j in range(len(name_list)-1):
        for (i) in range(j+1,len(name_list)):
            if name_list[j] in name_list[i]:
                answer = True
                break
            else:
                answer = False
        if answer == True:
            break
    return answer
print(check(name_list))


# #2
# seta = [1,2,3]
# setb = [1,2,4]
# def solution(arrayA, arrayB):
#     setA = list()
#     setB = list()
#
#     for i in arrayA:
#         if i not in setA:
#             setA.append(i)
#
#     for j in arrayB:
#         if j not in setB:
#             setB.append(j)
#
#     answer = [setA,setB,'합집합','차집합','교집합']
#
#     return answer
# print(solution(seta,setb))