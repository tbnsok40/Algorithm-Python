#####################코테####################
# 1번 문제, '봄'이 '봄봄'과 중복되는지 검사하는 것.
# 2번 문제, set() 메소드를 사용하지 않고, 합집합, 차집합, 교집합 등을 구하는 것

# name_list = ["가을", "우주", "너굴"]
# new_list = []
# def unique_string(name_list):
#     tmp_list = list()
#     for s in data:
#         if s in tmp_list:
#             return False
#         else:
#             tmp_list.append(s)
#     return True
seta = [1,2,3]
setb = [1,2,4]
def solution(arrayA, arrayB):
    setA = list()
    setB = list()

    for i in arrayA:
        if i not in setA:
            setA.append(i)

    for j in arrayB:
        if j not in setB:
            setB.append(j)

    answer = [setA,setB,'합집합','차집합','교집합']

    return answer
print(solution(seta,setb))